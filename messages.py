# Блок импортов для вывода ошибок
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from traceback import extract_stack


def _filename(file):
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


def show_error(text: str):
    colorama_init()
    print(f"{Fore.LIGHTRED_EX}Ошибка в файле " + _filename(extract_stack()[0].filename) + f" в строке " +
          str(extract_stack()[0].lineno) + f"{Style.RESET_ALL}: " + text)
    quit(-1)


def show_warning(text: str):
    colorama_init()
    print(f"{Fore.LIGHTYELLOW_EX}Предупреждение в файле " + _filename(extract_stack()[0].filename) + f" в строке " +
          str(extract_stack()[0].lineno) + f"{Style.RESET_ALL}: " + text)
