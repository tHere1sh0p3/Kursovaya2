import os
import shutil
from tkinter import *
from tkinter.ttk import Progressbar


def copy_files(source_folder, destination_folder):
    # Получаем список всех файлов в исходной папке
    files = os.listdir(source_folder)

    total_size = sum(
        os.path.getsize(os.path.join(source_folder, f))
        for f in files
        if os.path.isfile(os.path.join(source_folder, f))
    )
    copied_size = 0

    for file_name in files:
        source_file_path = os.path.join(source_folder, file_name)
        dest_file_path = os.path.join(destination_folder, file_name)

        if os.path.isfile(source_file_path):
            shutil.copyfile(source_file_path, dest_file_path)

            # Обновляем переменную с размером скопированных данных
            copied_size += os.path.getsize(source_file_path)

            # Рассчитываем процент выполненного процесса
            percent_complete = int((copied_size / total_size) * 100)

            # Обновляем прогрессбар
            progress_bar["value"] = percent_complete
            progress_bar.update()


# Функция запуска копирования
def start_copy():
    source_folder = entry_source.get()  # Входная директория
    destination_folder = entry_destination.get()  # Выходная директория

    try:
        copy_files(source_folder, destination_folder)
        print("Копирование завершено!")
    except Exception as e:
        print(f"Произошла ошибка при копировании: {e}")


# Создаем главное окно приложения
root = Tk()
root.title("Файловый менеджер")

# Поле ввода для источника
label_source = Label(root, text="Папка источник:")
label_source.grid(row=0, column=0, padx=10, pady=10)
entry_source = Entry(root, width=50)
entry_source.grid(row=0, column=1, padx=10, pady=10)

# Поле ввода для назначения
label_destination = Label(root, text="Папка назначение:")
label_destination.grid(row=1, column=0, padx=10, pady=10)
entry_destination = Entry(root, width=50)
entry_destination.grid(row=1, column=1, padx=10, pady=10)

# Кнопка начала копирования
button_start = Button(root, text="Начать копирование", command=start_copy)
button_start.grid(row=2, column=0, columnspan=2, pady=10)

# Прогрессбар
progress_bar = Progressbar(root, orient=HORIZONTAL,value= 50, length=400, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Запуск главного цикла приложения
root.mainloop()
