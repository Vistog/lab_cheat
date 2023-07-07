# Блок импортов для вывода ошибок
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from traceback import extract_stack
from tkinter import Tk, Button, Label


def _filename(file: str) -> str:
    """
    Внутренний метод, используемый для отбрасывания пути к файлу и получению только его названия,
    так же определяет тип файловой системы ОС.
    :param file: Путь к файлу, название которого нужно получить
    """
    if type(file) == str:
        # Определяем тип файловой системы
        os = ''
        for i in file:
            if i == '/':
                os = '/'
                break
            if i == '\\':
                os = '\\'
                break
        if os == '':
            return file
        return file[file.rfind(os) + 1::]
    else:
        colorama_init()
        show_error(f"Функция {Fore.YELLOW}_filename{Style.RESET_ALL} вместо объекта класса "
                   f"string получила {Fore.BLUE}" +
                   str(file) + f"{Style.RESET_ALL} типа {Fore.BLUE}" + str(type(file)) + f"{Style.RESET_ALL}.")


def show_error(text: str):
    """
    Используется для вывода ошибок с цветовым выделением. После выполнения завершает программу.
    :param text: Текст ошибки, возможно оформление с помощью библиотеки colorama.
    """
    colorama_init()
    # Проверка ввода
    if type(text) != str:
        show_error(f"Функция {Fore.YELLOW}show_error{Style.RESET_ALL} вместо объекта класса "
                   f"{Fore.BLUE}string{Style.RESET_ALL} получила {Fore.BLUE}" +
                   str(text) + f"{Style.RESET_ALL} типа {Fore.BLUE}" + str(type(text)) + f"{Style.RESET_ALL}.")

    print(f"{Fore.LIGHTRED_EX}Ошибка в файле " + _filename(extract_stack()[0].filename) + f" в строке " +
          str(extract_stack()[0].lineno) + f"{Style.RESET_ALL}: " + text)
    quit(-1)


def show_warning(text: str):
    """
    Используется для вывода предупреждений с цветовым выделением.
    :param text: Текст предупреждения, возможно оформление с помощью библиотеки colorama.
    """
    colorama_init()
    # Проверка ввода
    if type(text) != str:
        show_error(f"Функция {Fore.YELLOW}show_warning{Style.RESET_ALL} вместо объекта класса "
                   f"{Fore.BLUE}string{Style.RESET_ALL} получила {Fore.BLUE}" +
                   str(text) + f"{Style.RESET_ALL} типа {Fore.BLUE}" + str(type(text)) + f"{Style.RESET_ALL}.")

    print(f"{Fore.LIGHTYELLOW_EX}Предупреждение в файле " + _filename(extract_stack()[0].filename) + f" в строке " +
          str(extract_stack()[0].lineno) + f"{Style.RESET_ALL}: " + text)

def _place_window_in_center(win: Tk) -> Tk:
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def ask_question(title: str, text: str) -> bool:
    import ctypes

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    if type(text) != str:
        show_error(f"Функция {Fore.YELLOW}ask_question{Style.RESET_ALL} вместо объекта класса "
                   f"{Fore.BLUE}string{Style.RESET_ALL} получила {Fore.BLUE}" +
                   str(text) + f"{Style.RESET_ALL} типа {Fore.BLUE}" + str(type(text)) + f"{Style.RESET_ALL}.")
    if type(title) != str:
        show_error(f"Функция {Fore.YELLOW}ask_question{Style.RESET_ALL} вместо объекта класса "
                   f"{Fore.BLUE}string{Style.RESET_ALL} получила {Fore.BLUE}" +
                   str(title) + f"{Style.RESET_ALL} типа {Fore.BLUE}" + str(type(title)) + f"{Style.RESET_ALL}.")
    window = Tk()
    window.resizable(height=False, width=False)
    window.title(title)
    window.geometry("390x200")
    lab = Label(text=text)
    button_yes = Button(text="Да", height=2, width=7)
    button_no = Button(text="Нет", height=2, width=7)
    lab.pack(side='top')
    button_yes.pack(side="left", padx=30)
    button_no.pack(side="right", padx=30)
    _place_window_in_center(window)
    window.mainloop()
