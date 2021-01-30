import requests
from core import Degree, Course, Student


def api_url(route: str): return f"https://fenix.tecnico.ulisboa.pt/api/fenix/v1/{route}"


def validate_response(response) -> bool: return 200 <= response.status_code < 300


def error_response(response) -> None:
    print(f"Response Error: Status {response.status_code} and Reason {response.reason}")


def get_degrees(academic_year: str) -> list:
    response = requests.get(api_url("degrees"), data={"academicTerm": academic_year})

    if not validate_response(response):
        error_response(response)
        return []

    data = response.json()
    return [Degree(d['id'], d['name'], d['acronym'], d['academicTerm']) for d in data]
