import tkinter as tk

def open_window():
    # Проверяем, есть ли уже открытое окно
    if hasattr(open_window, 'window') and open_window.window.winfo_exists():
        print('Окно уже открыто!')
    else:
        # Создаем новое окно, если оно еще не было создано
        open_window.window = tk.Toplevel()
        open_window.window.title('Второе окно')
        
        def on_destroy(event):
            if hasattr(open_window, 'window'):
                del open_window.window
                
        open_window.window.protocol("WM_DELETE_WINDOW", lambda: on_destroy(None))
        open_window.window.bind("<Destroy>", on_destroy)
        
        btn_close = tk.Button(open_window.window, text='Закрыть', command=open_window.window.destroy)
        btn_close.pack(pady=10)

# Создаем главное окно
root = tk.Tk()
root.title('Главное окно')

# Кнопка для открытия второго окна
btn_open = tk.Button(root, text='Открыть окно', command=open_window)
btn_open.pack(pady=10)

# Запускаем главный цикл
root.mainloop()