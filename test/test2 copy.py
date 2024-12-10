import os
import sys
import tkinter as tk
from tkinter import PhotoImage, Entry, Label, Button, Canvas


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x500")
        self.root.configure(bg="#eea155")
        self.root.title("CalculatorBZU")
        
        self.canvas = tk.Canvas(
            self.root,
            bg="#eea155",
            width=750,
            height=500,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.load_assets()
        self.create_widgets()
    
    def load_asset(self, path):
        base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        assets = os.path.join(base, "assets")
        return os.path.join(assets, path)

    def load_assets(self):
        self.image_1 = tk.PhotoImage(file=self.load_asset("1.png"))
        self.button_1_image = tk.PhotoImage(file=self.load_asset("2.png"))
        self.button_2_image = tk.PhotoImage(file=self.load_asset("3.png"))
        self.button_3_image = tk.PhotoImage(file=self.load_asset("4.png"))

    def create_widgets(self):
        self.canvas.create_image(389, 298, image=self.image_1)

        self.button_1 = tk.Button(
            image=self.button_1_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 has been pressed!"),
        )
        self.button_1.place(x=137, y=299, width=107, height=24)

        self.button_2 = tk.Button(
            image=self.button_2_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 has been pressed!"),
        )
        self.button_2.place(x=693, y=439, width=50, height=50)

        self.button_3 = tk.Button(
            image=self.button_3_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 has been pressed!"),
        )
        self.button_3.place(x=622, y=439, width=50, height=50)

        self.textbox_1 = TkForge_Entry(
            self.root,
            bd=0,
            bg="#f5f5f5",
            fg="#594129",
            placeholder="Количество углеводов",
            insertbackground="#594129",
            highlightthickness=0,
            font=("tilda sans medium", 18 * -1),
        )
        self.textbox_1.place(x=82, y=124, width=229, height=30)

        self.textbox_2 = TkForge_Entry(
            self.root,
            bd=0,
            bg="#f5f5f5",
            fg="#594129",
            placeholder="Количество жиров",
            insertbackground="#594129",
            highlightthickness=0,
            font=("tilda sans medium", 18 * -1),
        )
        self.textbox_2.place(x=82, y=184, width=229, height=30)

        self.textbox_3 = TkForge_Entry(
            self.root,
            bd=0,
            bg="#f5f5f5",
            fg="#594129",
            placeholder="Количество белков",
            insertbackground="#594129",
            highlightthickness=0,
            font=("tilda sans medium", 18 * -1),
        )
        self.textbox_3.place(x=82, y=245, width=229, height=30)

        self.label_1 = tk.Label(
            self.root,
            text='Нажмите "Рассчитать"',
            anchor="nw",
            bg="#f5f5f5",
            fg="#594129",
            font=("tilda sans medium", 18 * -1),
        )
        self.label_1.place(x=82, y=347)

        self.root.resizable(False, False)
    
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
        
        button_open_calculator = Button(self, text="Открыть калькулятор IMT", command=self.open_calculator)
        button_open_calculator.pack(pady=20)
    
    def open_calculator(self):
        calculator_window = CalculatorApp(master=self)
        calculator_window.grab_set()  # Блокируем главное окно до закрытия дочернего

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

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()