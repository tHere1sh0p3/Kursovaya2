from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

label_style = ttk.Style()
label_style.configure(
    "My.TLabel",  # имя стиля
    font="arial 22",  # шрифт
    foreground="#004D40",  # цвет текста
    padding=10,  # отступы
    background="#B2DFDB",
)  # фоновый цвет

label = ttk.Label(text="Hello World", style="My.TLabel")
label.pack(anchor=CENTER, expand=1)

root.mainloop()
