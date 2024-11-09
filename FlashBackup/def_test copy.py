import ctypes
import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

import psutil

def update_flash_drives():
    # Получаем список доступных флешек
    drives = []
    for disk in range(65, 91):  # от A до Z
        drive = f"{chr(disk)}:"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

def get_volume_label(drive):
    try:
        label = ctypes.create_unicode_buffer(255)
        ctypes.windll.kernel32.GetVolumeInformationW(
            drive, label, 255, None, None, None, None, None
        )
        return label.value
    except Exception as e:
        return str(e)

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


if __name__ == "__main__":
    drives = get_usb_drives()

def is_system_folder(folder_name):
    # Проверка, является ли папка системной
    return folder_name in ['System Volume Information', '$RECYCLE.BIN']

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

        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при копировании {item}: {e}")

    messagebox.showinfo("Успех", "Файлы успешно скопированы!")

def select_destination_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder)

def start_copy():
    flash_drive = flash_combobox.get()
    destination_folder = destination_entry.get()
    if flash_drive and destination_folder:
        copy_files_from_flash_drive(flash_drive, destination_folder)
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, выберите флешку и папку назначения.")

# Создание GUI (предполагая, что у вас есть оставшаяся часть интерфейса)
root = tk.Tk()
root.title("Копирование с флешки")

flash_combobox = ttk.Combobox(root, values=update_flash_drives())
flash_combobox.pack(pady=10)

destination_entry = tk.Entry(root)
destination_entry.pack(pady=10)

select_button = tk.Button(root, text="Выбрать папку назначения", command=select_destination_folder)
select_button.pack(pady=10)

copy_button = tk.Button(root, text="Копировать", command=start_copy)
copy_button.pack(pady=10)

root.mainloop()