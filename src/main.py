from collections import Callable
from selectmenu import SelectMenu
from utils import clear_screen, bold, clear_before


def error_menu(message: str, again_action: Callable, back_action: Callable):
    print('')
    return SelectMenu(
        message=f"Error: {message}",
        choices={'1. Try again': again_action, '2. Go back': lambda: clear_before(back_action)}
    )


def action_exit():
    clear_screen()
    print("Thank you for using Delegate Helper!")
    print("Have a great day :)")
    print("\n")
    print(bold("Exited successfully!"))
    exit(0)


if __name__ == "__main__":
    start_menu = SelectMenu({
        '0. Exit': action_exit
    }, message='Start Menu')

    clear_screen()

    start_menu.select_action()
