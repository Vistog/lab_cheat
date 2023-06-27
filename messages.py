# Блок импортов для вывода ошибок
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from traceback import extract_stack


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
