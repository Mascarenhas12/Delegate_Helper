from collections import Callable
from selectmenu import SelectMenu
from utils import clear_screen, bold, clear_before
import api


def error_menu(message: str, again_action: Callable, back_action: Callable):
    print('')
    return SelectMenu(
        message=f"Error: {message}",
        choices={'1. Try again': again_action, '2. Go back': lambda: clear_before(back_action)}
    )


def change_selected_degree(degree_id: str) -> None:
    global selected_degree
    selected_degree = degree_id


def change_selected_course(course_id: str) -> None:
    global selected_course
    selected_course = course_id


def action_exit():
    clear_screen()
    print("Thank you for using Delegate Helper!")
    print("Have a great day :)")
    print("\n")
    print(bold("Exited successfully!"))
    exit(0)


def action_list_course_students(course_id: str):

    if course_id == "":
        return list_menu.select_action(message="First Select a Course!", clear_before=True)

    clear_screen()
    students = api.get_course_students(course_id)
    studs = sorted([s for s in students], key=lambda s: s.username)

    for s in studs:
        print(s
              )
    return list_menu.select_action()


def action_list_degree_courses(degree_id: str):

    if degree_id == "":
        return list_menu.select_action(message="First Select a Degree!", clear_before=True)

    clear_screen()
    courses = api.get_degree_courses(degree_id)
    cors = sorted([c for c in courses], key=lambda c: c.acronym)

    course_menu = SelectMenu({
    }, message='Course Selection Menu')

    opt = 0
    choices = []
    for cor in cors:
        opt += 1
        choices.append(f"{opt}. {cor}")

    course_menu.add_choices(choices)
    result = course_menu.select()
    print(bold(result[2:]))
    change_selected_course(cors[choices.index(result)].id)

    return list_menu.select_action()


def action_list_degrees():
    clear_screen()
    degrees = api.get_degrees()
    degs = sorted([d for d in degrees if d.acronym[0] == 'M' or d.acronym[0] == 'L'], key=lambda d: d.acronym)

    degree_menu = SelectMenu({
    }, message='Degree Selection Menu')

    opt = 0
    choices = []
    for deg in degs:
        opt += 1
        choices.append(f"{opt}. {deg}")

    degree_menu.add_choices(choices)
    result = degree_menu.select()
    print(bold(result[2:]))
    change_selected_degree(degs[choices.index(result)].id)

    return list_menu.select_action()


if __name__ == "__main__":
    selected_degree = ""
    selected_course = ""

    start_menu = SelectMenu({
        '1. List students in Course': lambda: list_menu.select_action(clear_before=True),
        '0. Exit': action_exit
    }, message='Start Menu')

    list_menu = SelectMenu({
        '1. List and Set Degree': action_list_degrees,
        '2. List and Set Degree Course': lambda: action_list_degree_courses(degree_id=selected_degree),
        '3. List Students in Course': lambda: action_list_course_students(course_id=selected_course),
        '0. Return To Start Menu': lambda: start_menu.select_action(clear_before=True),
        '-1. Exit': action_exit
    }, message='List Selection Menu')

    clear_screen()

    start_menu.select_action()
