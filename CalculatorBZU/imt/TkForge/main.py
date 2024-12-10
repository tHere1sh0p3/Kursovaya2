import os
import sys
import tkinter as tk


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


window = tk.Tk()
window.geometry("400x500")
window.configure(bg="#eea255")
window.title("CalculatorIMT")

canvas = tk.Canvas(
    window,
    bg="#eea255",
    width=400,
    height=500,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)

image_1 = tk.PhotoImage(file=load_asset("1.png"))

canvas.create_image(199, 248, image=image_1)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 has been pressed!"),
)

button_1.place(x=146, y=333, width=107, height=24)

textbox_1 = tk.Entry(
    bd=0, 
    bg="#f5f5f5", 
    fg="#594129", 
    insertbackground="#594129", 
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)

textbox_1.place(x=85, y=191, width=229, height=30)

textbox_2 = tk.Entry(
    bd=0, 
    bg="#f5f5f5", 
    fg="#594129", 
    insertbackground="#594129", 
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)

textbox_2.place(x=85, y=271, width=229, height=30)

label_1 = tk.Label(
    text='Нажмите "Рассчитать"',  
    anchor="c",  
    bg="#f5f5f5",
    fg="#594129", 
    font=("tilda sans medium", 18 * -1),
)

label_1.place(x=105, y=394)

window.resizable(False, False)
window.mainloop()
