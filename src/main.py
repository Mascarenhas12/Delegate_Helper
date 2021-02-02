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


def change_selected_degrees(degrees: list) -> None:
    global selected_degrees
    selected_degrees = degrees


def change_selected_courses(courses: list) -> None:
    global selected_courses
    selected_courses = courses


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


# noinspection DuplicatedCode
def action_cross_course_students(courses: list):

    if not courses:
        return cross_menu.select_action(message="First Select a Course!", clear_before=True)

    clear_screen()

    students = api.get_course_students(courses[0])
    for course_id in courses:
        temp = api.get_course_students(course_id)
        students = filter(lambda x: x in temp, students)

    studs = sorted([s for s in students], key=lambda s: s.username)

    for s in studs:
        print(s)

    return cross_menu.select_action()


# noinspection DuplicatedCode
def action_cross_degree_courses(degrees: list):
    if not degrees:
        return cross_menu.select_action(message="First Select a Degree!", clear_before=True)

    clear_screen()
    courses = api.get_degree_courses(degrees[0])
    for degree_id in degrees:
        temp = api.get_degree_courses(degree_id)
        for x in temp:
            if x not in courses:
                courses.append(x)

    cors = sorted([c for c in courses], key=lambda c: c.acronym)

    course_menu = SelectMenu({
    }, message='Course Selection Menu')

    opt = 0
    choices = []
    for cor in cors:
        opt += 1
        choices.append(f"{opt}. {cor}")

    choices.append("0. Confirm Selection")
    course_menu.add_choices(choices)

    selections = []
    result = course_menu.select()

    while result != "0. Confirm Selection":
        index = choices.index(result)
        if cors[index].id not in selections:
            selections.append(cors[index].id)
            course_menu.choices[index] += "«"
        else:
            selections.pop(selections.index(cors[index].id))
            course_menu.choices[index] = course_menu.choices[index][:-1]
        result = course_menu.select()

    change_selected_courses(selections)

    return cross_menu.select_action()


# noinspection DuplicatedCode
def action_cross_degrees():
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

    choices.append("0. Confirm Selection")
    degree_menu.add_choices(choices)

    selections = []
    result = degree_menu.select()

    while result != "0. Confirm Selection":
        index = choices.index(result)
        if degs[index].id not in selections:
            selections.append(degs[index].id)
            degree_menu.choices[index] += "«"
        else:
            selections.pop(selections.index(degs[index].id))
            degree_menu.choices[index] = degree_menu.choices[index][:-1]
        result = degree_menu.select()

    change_selected_degrees(selections)
    return cross_menu.select_action()


if __name__ == "__main__":
    selected_degree = ""
    selected_course = ""
    selected_degrees = []
    selected_courses = []

    start_menu = SelectMenu({
        '1. List students in Course': lambda: list_menu.select_action(clear_before=True),
        '2. Cross Reference students in Courses': lambda: cross_menu.select_action(clear_before=True),
        '0. Exit': action_exit
    }, message='Start Menu')

    list_menu = SelectMenu({
        '1. List and Set Degree': action_list_degrees,
        '2. List and Set Degree Course': lambda: action_list_degree_courses(degree_id=selected_degree),
        '3. List Students in Course': lambda: action_list_course_students(course_id=selected_course),
        '0. Return To Start Menu': lambda: start_menu.select_action(clear_before=True),
        '-1. Exit': action_exit
    }, message='List Selection Menu')

    cross_menu = SelectMenu({
        '1. List and Cross Degrees': action_cross_degrees,
        '2. List and Cross Degrees Courses': lambda: action_cross_degree_courses(degrees=selected_degrees),
        '3. Cross Students in Courses': lambda: action_cross_course_students(courses=selected_courses),
        '0. Return To Start Menu': lambda: start_menu.select_action(clear_before=True),
        '-1. Exit': action_exit
    }, message='Cross Selection Menu')

    clear_screen()

    start_menu.select_action()
