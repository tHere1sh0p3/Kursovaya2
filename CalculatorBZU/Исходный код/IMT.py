import os
import sys
import re
import tkinter as tk
from tkinter import PhotoImage, Entry, Label, Button, Canvas
from tkinter import messagebox

def is_valid(newval):
    # Проверяет, соответствует ли введенное значение шаблону регулярного выражения (начинается с '+' или цифры, длина до 11 символов)
    return re.match(r"^\+{0,1}\d{0,11}$", newval) is not None



class CalculatorIMTWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.configure(bg="#eea255")
        self.title("CalculatorIMT")
        self.resizable(False, False)

        # Создаем canvas
        self.canvas = Canvas(
            self,
            bg="#eea255",
            width=400,
            height=500,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)
        check = (self.register(is_valid), "%P")

        # Загружаем изображения
        self.image_1 = PhotoImage(file=self.load_asset("1_imt.png"))
        self.button_1_image = PhotoImage(file=self.load_asset("2_imt.png"))

        # Размещаем элементы интерфейса
        self.canvas.create_image(199, 248, image=self.image_1)

        self.textbox1 = Entry(
            self,
            bd=0,
            bg="#f5f5f5",
            fg="#594129",
            insertbackground="#594129",
            highlightthickness=0,
            font=("tilda sans medium", 18 * -1),
        )
        self.textbox1.place(x=85, y=191, width=229, height=30)
        self.textbox1.config(validate="key", validatecommand=check)

        self.textbox_2 = Entry(
            self,
            bd=0,
            bg="#f5f5f5",
            fg="#594129",
            insertbackground="#594129",
            highlightthickness=0,
            font=("tilda sans medium", 18 * -1),
        )
        self.textbox_2.place(x=85, y=271, width=229, height=30)
        self.textbox_2.config(validate="key", validatecommand=check)

        self.label_1 = Label(
            self,
            text='Нажмите "Рассчитать"',
            anchor="c",
            bg="#f5f5f5",
            fg="#594129",
            font=("tilda sans medium", 18 * -1),
        )
        self.label_1.place(x=85, y=394)

        self.button_1 = Button(
            self,
            image=self.button_1_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.calcIMT,
        )
        self.button_1.place(x=146, y=333, width=107, height=24)

    def calcIMT(self):
        h = self.textbox1.get()
        w = self.textbox_2.get()
        if h and w:
            h = float(h) / 100
            w = float(w)
            result = (w / (h * h))
            # Вычисление результата по формуле и установка его в текст метки
            self.label_1["text"] = (f'{result:.1f}')
        else:
            messagebox.showwarning(
                "Внимание", "Пожалуйста, введите данные в программу."
            )

    @staticmethod
    def load_asset(path):
        base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        assets = os.path.join(base, "assets")
        return os.path.join(assets, path)
    
    

# Класс главного окна
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное окно")
        self.geometry("300x200")

        button_open_calculator = Button(
            self,
            text="Открыть калькулятор IMT",
            command=self.open_calculator,
        )
        button_open_calculator.pack(pady=20)

    def open_calculator(self):
        calculator_window = CalculatorIMTWindow()
        calculator_window.grab_set()  # Блокируем главное окно до закрытия дочернего


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
