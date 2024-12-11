# Импорт модуля os для работы с файловой системой
import os

# Импорт модуля re для работы с регулярными выражениями
import re

# Импорт модуля sys для доступа к системным функциям и переменным
import sys

# Импорт модуля webbrowser для открытия веб-браузера
import webbrowser

# Импорт модуля tkinter под псевдонимом tk для создания графического интерфейса
import tkinter as tk

# Дополнительный импорт всех классов и функций из tkinter без необходимости использовать префикс tk
from tkinter import *
from tkinter import ttk

from IMT import CalculatorIMTWindow


# Создание класса TkForge_Entry, который наследует от виджета Entry в tkinter
class TkForge_Entry(tk.Entry):
    # Конструктор класса, принимающий параметры master (родительский элемент) и kwargs (аргументы для виджетов)
    def __init__(
        self, master=None, placeholder="Enter text", placeholder_fg="#594129", **kwargs
    ):

        # Вызов конструктора родительского класса tk.Entry
        super().__init__(master, **kwargs)

        # Сохранение параметров placeholder и placeholder_fg в качестве атрибутов класса
        self.p, self.p_fg, self.fg = placeholder, placeholder_fg, self.cget("fg")

        # Вставка текста-заполнителя в виджет
        self.putp()

        # Привязка события получения фокуса (<FocusIn>) к методу toggle
        self.bind("<FocusIn>", self.toggle)

        # Привязка события потери фокуса (<FocusOut>) к методу toggle
        self.bind("<FocusOut>", self.toggle)

    # Метод для вставки заполнителя в виджет
    def putp(self):
        # Очистка содержимого виджета
        self.delete(0, tk.END)

        # Вставка текста-заполнителя
        self.insert(0, self.p)

        # Установка цвета шрифта для заполнителя
        self.config(fg=self.p_fg)

        # Установка флага, показывающего, что виджет содержит заполнитель
        self.p_a = True

    # Метод для переключения между состоянием заполнителя и обычным текстом при получении/потере фокуса
    def toggle(self, event):
        # Если виджет содержит заполнитель, удалить его и установить обычный цвет шрифта
        if self.p_a:
            self.delete(0, tk.END)
            self.config(fg=self.fg)
            self.p_a = False

        # Если виджет пуст после потери фокуса, вставить заполнитель обратно
        elif not self.get():
            self.putp()

    # Переопределенный метод get для возврата значения виджета, исключая случай, когда он содержит заполнитель
    def get(self):
        # Возвращает пустую строку, если виджет содержит заполнитель, иначе возвращает содержимое виджета
        return "" if self.p_a else super().get()

    # Метод для установки состояния заполнителя вручную
    def is_placeholder(self, b):
        # Устанавливает флаг p_a и соответствующий цвет шрифта
        self.p_a = b
        self.config(fg=self.p_fg if b == True else self.fg)

    # Метод для получения текущего текста-заполнителя
    def get_placeholder(self):
        # Возвращает текущий текст-заполнитель
        return self.p


# Функция для загрузки ресурсов из папки assets
def load_asset(path):
    # Получение пути к текущей директории или директории сборки (если приложение упаковано)
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

    # Построение полного пути до папки assets
    assets = os.path.join(base, "assets")

    # Построение полного пути до ресурса
    return os.path.join(assets, path)


# Функция для проверки валидности введенного числа
def is_valid(newval):
    # Проверяет, соответствует ли введенное значение шаблону регулярного выражения (начинается с '+' или цифры, длина до 11 символов)
    return re.match(r"^\+{0,1}\d{0,11}$", newval) is not None


# Функция для расчета результата на основе значений из трех текстовых полей
def calculate():
    # Получение значения из первого текстового поля, преобразование его в целое число
    p = textbox_1.get()
    p = int(p)

    # Получение значения из второго текстового поля, преобразование его в целое число
    f = textbox_2.get()
    f = int(f)

    # Получение значения из третьего текстового поля, преобразование его в целое число
    c = textbox_3.get()
    c = int(c)

    # Вычисление результата по формуле и установка его в текст метки
    label["text"] = str(p * 4 + f * 9 + c * 4)


# Функция для создания нового окна
def open_window():
    # Проверяем, есть ли уже открытое окно
    if (
        hasattr(open_window, "window")
        and isinstance(open_window.window, CalculatorIMTWindow)
        and open_window.window.winfo_exists()
    ):
        print("Окно уже открыто!")
    else:
        # Создаем новое окно, если оно еще не было создано
        open_window.window = CalculatorIMTWindow()

        def on_destroy(event):
            if hasattr(open_window, "window"):
                del open_window.window


# Создание главного окна приложения
root = Tk()

# Задание размеров окна
root.geometry("750x500")

# Задание фона окна
root.configure(bg="#eea155")

# Задание заголовка окна
root.title("CalculatorBZU")

# Переменная для хранения количества кликов
click = 0

# Создание холста для размещения элементов
canvas = tk.Canvas(
    root,
    bg="#eea155",
    width=750,
    height=500,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

# Размещение холста в окне
canvas.place(x=0, y=0)

# Загрузка изображения и создание объекта PhotoImage
image_1 = tk.PhotoImage(file=load_asset("1.png"))

# Размещение изображения на холсте
canvas.create_image(385, 298, image=image_1)

# Регистрация функции is_valid для использования в качестве валидатора ввода
check = (root.register(is_valid), "%P")

# Переменная для хранения сообщения об ошибке
errmsg = str()

# Создание текстового поля с заполнителем "Количество углеводов"
textbox_1 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество углеводов",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)

# Размещение текстового поля на экране
textbox_1.place(x=82, y=124, width=229, height=30)

# Настройка валидации ввода для текстового поля
textbox_1.config(validate="key", validatecommand=check)

# Создание текстового поля с заполнителем "Количество жиров"
textbox_2 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество жиров",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)

# Размещение текстового поля на экране
textbox_2.place(x=82, y=184, width=229, height=30)

# Настройка валидации ввода для текстового поля
textbox_2.config(validate="key", validatecommand=check)

# Создание текстового поля с заполнителем "Количество белков"
textbox_3 = TkForge_Entry(
    bd=0,
    bg="#f5f5f5",
    fg="#594129",
    placeholder="Количество белков",
    insertbackground="#594129",
    highlightthickness=0,
    font=("tilda sans medium", 18 * -1),
)

# Размещение текстового поля на экране
textbox_3.place(x=82, y=245, width=229, height=30)

# Настройка валидации ввода для текстового поля
textbox_3.config(validate="key", validatecommand=check)

# Загрузка изображения для кнопки
button_1_image = tk.PhotoImage(file=load_asset("2.png"))

# Создание кнопки с изображением и привязкой к функции calculate
button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=calculate,
)

# Размещение кнопки на экране
button_1.place(x=137, y=299, width=107, height=24)

# Загружаем изображение для второй кнопки из файла "3.png" в папке "assets"
button_2_image = tk.PhotoImage(file=load_asset("3.png"))

# Создаем вторую кнопку с загруженным изображением, плоской рамкой, нулевой толщиной границы и командой для открытия ссылки в браузере
button_2 = tk.Button(
    image=button_2_image,  # Используем загруженное изображение
    relief="flat",  # Делаем кнопку плоской
    borderwidth=0,  # Убираем толщину рамки
    highlightthickness=0,  # Убираем выделение при фокусе
    command=lambda: webbrowser.open(
        "https://github.com/tHere1sh0p3/Kursovaya2"
    ),  # Открываем ссылку при нажатии на кнопку
)

# Размещаем вторую кнопку на экране по указанным координатам и размерам
button_2.place(x=688, y=439, width=50, height=50)

# Загружаем изображение для третьей кнопки из файла "5.png" в папке "assets"
button_3_image = tk.PhotoImage(file=load_asset("5.png"))

# Создаем третью кнопку с загруженным изображением, плоской рамкой, нулевой толщиной границы и командой для вызова функции click123
button_3 = tk.Button(
    image=button_3_image,  # Используем загруженное изображение
    relief="flat",  # Делаем кнопку плоской
    borderwidth=0,  # Убираем толщину рамки
    highlightthickness=0,  # Убираем выделение при фокусе
    command=open_window,  # Вызываем функцию click123 при нажатии на кнопку
)

# Размещаем третью кнопку на экране по указанным координатам и размерам
button_3.place(x=618, y=439, width=50, height=50)

# Создаем метку с текстом 'Нажмите "Рассчитать"', выравниванием по северо-западу, цветом фона, цветом текста и определенным шрифтом
label = tk.Label(
    text='Нажмите "Рассчитать"',  # Указываем текст метки
    anchor="nw",  # Выравниваем текст по северо-западному углу
    bg="#f5f5f5",  # Устанавливаем белый фон
    fg="#594129",  # Устанавливаем коричневый цвет текста
    font=("tilda sans medium", 18 * -1),  # Определяем шрифт и размер текста
)

# Размещаем метку на экране по указанным координатам и размерам
label.place(x=82, y=347, width=229, height=30)

# Запрещаем изменение размеров окна пользователем
root.resizable(False, False)

# Запускаем основной цикл обработки событий программы
if __name__ == "__main__":
    root.mainloop()
