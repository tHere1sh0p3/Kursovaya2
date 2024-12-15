import os
import re
import sys
import shutil
import psutil
import ctypes
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog


class TkForge_Entry(tk.Entry):
    def __init__(
        self, master=None, placeholder="Enter text", placeholder_fg="grey", **kwargs
    ):
        super().__init__(master, **kwargs)

        self.p, self.p_fg, self.fg = placeholder, placeholder_fg, self.cget("fg")
        self.putp()
        self.bind("<FocusIn>", self.toggle)
        self.bind("<FocusOut>", self.toggle)

    def putp(self):
        self.delete(0, tk.END)
        self.insert(0, self.p)
        self.config(fg=self.p_fg)
        self.p_a = True

    def toggle(self, event):
        if self.p_a:
            self.delete(0, tk.END)
            self.config(fg=self.fg)
            self.p_a = False
        elif not self.get():
            self.putp()

    def get(self):
        return "" if self.p_a else super().get()

    def is_placeholder(self, b):
        self.p_a = b
        self.config(fg=self.p_fg if b == True else self.fg)

    def get_placeholder(self):
        return self.p


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


# Функция для получения метки тома
def get_volume_label(drive):
    try:
        label = ctypes.create_unicode_buffer(255)
        ctypes.windll.kernel32.GetVolumeInformationW(
            drive, label, 255, None, None, None, None, None
        )
        return label.value
    except Exception as e:
        return str(e)

# Получение списка USB-накопителей
def get_usb_drives():
    usb_drives = []
    for part in psutil.disk_partitions():
        if "removable" in part.opts:
            label = get_volume_label(part.device)
            usage = psutil.disk_usage(part.mountpoint)
            usb_drives.append(
                f"{label} ({part.mountpoint}) [{usage.total / (1024 ** 3):.1f} ГБ]"
            )
    return usb_drives

# Выбор выходной директории
def select_outpath():
    path = filedialog.askdirectory()
    if path:
        textbox_1.delete(0, tk.END)
        textbox_1.is_placeholder(False)
        textbox_1.insert(0, path)

# Проверка, является ли папка системной
def is_system_folder(folder_name):
    return folder_name in ["System Volume Information", "$RECYCLE.BIN"]

# Копирование файлов с USB-накопителя
def copy_files_from_flash_drive(flash_drive_path, destination_folder):
    if not os.path.exists(flash_drive_path):
        messagebox.showerror("Ошибка", f"Флешка по пути {flash_drive_path} не найдена.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for item in os.listdir(flash_drive_path):
        source_path = os.path.join(flash_drive_path, item)

        # Пропускаем системные папки
        if is_system_folder(item):
            continue

        destination_path = os.path.join(destination_folder, item)

        def copy_item():
            try:
                if os.path.isfile(source_path):
                    shutil.copy2(source_path, destination_path)
                elif os.path.isdir(source_path):
                    shutil.copytree(source_path, destination_path)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при копировании {item}: {e}")
        
        # Создаем поток для копирования файла/директории
        thread = threading.Thread(target=copy_item)
        thread.start()

    messagebox.showinfo("Успех", "Файлы успешно скопированы!")

# Извлечение пути к диску из строки
def extract_disk_path(input_string):
    match = re.search(r'$([A-Z]:\$$', input_string)
    if match:
        return match.group(1)
    else:
        return None

# Начало копирования
def start_copy():
    selected_string = combobox.get()
    disk_path = extract_disk_path(selected_string)
    flash_drive = disk_path
    destination_folder = textbox_1.get()
    if flash_drive and destination_folder:
        copy_files_from_flash_drive(flash_drive, destination_folder)
    else:
        messagebox.showwarning(
            "Warning", "Please, choose a USB drive and a path to copy."
        )

if __name__ == "__main__":
    drives = get_usb_drives()

window = tk.Tk()
window.geometry("300x350")
window.configure(bg="#808080")
window.title("FlashBackup")

image_1 = tk.PhotoImage(file=load_asset("1.png"))

canvas = tk.Canvas(
    window,
    bg="#808080",
    width=300,
    height=350,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)
canvas.create_image(153, 166, image=image_1)

combobox = ttk.Combobox(
    values=drives,
    width=17,
)
combobox.pack(anchor="ne", padx=14, pady=9)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))
button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=select_outpath,
)
button_1.place(x=247, y=240, width=21, height=16)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))
button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=start_copy,
)
button_2.place(x=77, y=287, width=146, height=33)

textbox_1 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#000000",
    placeholder="Backup path",
    insertbackground="#000000",
    highlightthickness=0,
    font=("tilda sans medium", 13),
)
textbox_1.place(x=31, y=237, width=209, height=23)

window.resizable(False, False)
window.mainloop()
