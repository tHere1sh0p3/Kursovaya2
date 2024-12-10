import os
import sys
import tkinter as tk
from tkinter import *


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


window = tk.Tk()
window.geometry("750x500")
window.configure(bg="#eea155")
window.title("CalculatorBZU")

canvas = tk.Canvas(
    window,
    bg="#eea155",
    width=750,
    height=500,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)


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


image_1 = tk.PhotoImage(file=load_asset("1.png"))

canvas.create_image(389, 298, image=image_1)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 has been pressed!"),
)

button_1.place(x=137, y=299, width=107, height=24)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))

button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 has been pressed!"),
)

button_2.place(x=693, y=439, width=50, height=50)

button_3_image = tk.PhotoImage(file=load_asset("4.png"))

button_3 = tk.Button(
    image=button_3_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 has been pressed!"),
)

button_3.place(x=622, y=439, width=50, height=50)

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

label_1 = tk.Label(text='Нажмите "Рассчитать"',  # Указываем текст метки
    anchor="nw",  # Выравниваем текст по северо-западному углу
    bg="#f5f5f5",  # Устанавливаем белый фон
    fg="#594129",  # Устанавливаем коричневый цвет текста
    font=("tilda sans medium", 18 * -1),  # Определяем шрифт и размер текста
)
label_1.place(x=82, y=347)

window.resizable(False, False)
window.mainloop()
