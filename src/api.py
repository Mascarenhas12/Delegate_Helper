import requests
from core import Degree, Course, Student

ACADEMIC_YEAR = "2020/2021"


def api_url(route: str): return f"https://fenix.tecnico.ulisboa.pt/api/fenix/v1/{route}"


def validate_response(response) -> bool: return 200 <= response.status_code < 300


def error_response(response) -> None:
    print(f"Response Error: Status {response.status_code} and Reason {response.reason}")


def get_degrees() -> list:
    response = requests.get(api_url("degrees"), data={"academicTerm": ACADEMIC_YEAR})

    if not validate_response(response):
        error_response(response)
        exit(-1)

    data = response.json()
    return [Degree(d['id'], d['name'], d['acronym'], d['academicTerm']) for d in data]


def get_degree_courses(degree_id: str) -> list:
    response = requests.get(api_url(f"degrees/{degree_id}/courses"), data={"academicTerm": ACADEMIC_YEAR})

    if not validate_response(response):
        error_response(response)
        exit(-1)

    data = response.json()
    return [Course(d['id'], d['name'], d['acronym'], d['academicTerm']) for d in data]


def get_course_students(course_id: str) -> list:
    response = requests.get(api_url(f"courses/{course_id}/students"), data={"academicTerm": ACADEMIC_YEAR})

    if not validate_response(response):
        error_response(response)
        exit(-1)

    data = response.json()
    return [Student(d['username'], d['degree']['acronym']) for d in data['students']]
