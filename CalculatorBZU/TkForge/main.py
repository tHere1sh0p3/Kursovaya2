import os  # Импортируем модуль os
import sys  # Импортируем модуль sys
import tkinter as tk  # Импортируем модуль tkinter задаем ему синононим tk
import webbrowser  # Импортируем модуль webbrowser
import re  # Импортируем модуль re
from tkinter import *
from tkinter import ttk


class TkForge_Entry(tk.Entry):
    def __init__(
        self, master=None, placeholder="Enter text", placeholder_fg="#594129", **kwargs
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


class Window(Tk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title("Новое окно")
        self.geometry("250x200")

        # определение кнопки
        self.button = ttk.Button(self, text="закрыть")
        self.button["command"] = self.button_clicked
        self.button.pack(anchor="center", expand=1)

    def button_clicked(self):
        self.destroy()


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


def is_valid(newval):
    return re.match("^\+{0,1}\d{0,11}$", newval) is not None


def calculate():
    p = textbox_1.get()
    p = int(p)
    f = textbox_2.get()
    f = int(f)
    c = textbox_3.get()
    c = int(c)
    label["text"] = str(p * 4 + f * 9 + c * 4)


def click123():
    window = Window()

root = Tk()
root.geometry("750x500")
root.configure(bg="#eea155")
root.title("CalculatorBZU")
click = 0

canvas = tk.Canvas(
    root,
    bg="#eea155",
    width=750,
    height=500,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)


image_1 = tk.PhotoImage(file=load_asset("1.png"))

canvas.create_image(394, 306, image=image_1)


check = (root.register(is_valid), "%P")

errmsg = str()

textbox_1 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество углеводов",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)
textbox_1.place(x=82, y=124, width=229, height=30)
textbox_1.config(validate="key", validatecommand=check)

textbox_2 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество жиров",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)
textbox_2.place(x=82, y=184, width=229, height=30)
textbox_2.config(validate="key", validatecommand=check)

textbox_3 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество белков",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)
textbox_3.place(x=82, y=245, width=229, height=30)
textbox_3.config(validate="key", validatecommand=check)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))
button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=calculate,
)
button_1.place(x=137, y=299, width=107, height=24)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))
button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://github.com/tHere1sh0p3/Kursovaya2"),
)
button_2.place(x=688, y=439, width=50, height=50)

button_3_image = tk.PhotoImage(file=load_asset("5.png"))
button_3 = tk.Button(
    image=button_3_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=click123,
)
button_3.place(x=618, y=439, width=50, height=50)

label = tk.Label(
    text='Нажмите "Рассчитать"',
    anchor="nw",
    foreground="#594129",
    font=("tilda sans medium", 18 * -1),
)
label.place(x=82, y=347, width=229, height=30)

root.resizable(False, False)
root.mainloop()
