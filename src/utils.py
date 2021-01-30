import os
from typing import Callable


def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def clear_before(func: Callable):
    clear_screen()
    func()


def bold(text: str) -> str:
    return "\033[1m" + text + "\033[0m"
