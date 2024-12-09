from tkinter import *
from tkinter import ttk
 
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
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
def click():
    window = Window()
 
open_button = ttk.Button(text="Создать окно", command=click)
open_button.pack(anchor="center", expand=1)
 
root.mainloop()