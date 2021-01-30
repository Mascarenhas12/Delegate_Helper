class Degree:
    def __init__(self, id: str, name: str, acronym: str, academic_years: list):
        self.id = id
        self.name = name
        self.acronym = acronym
        self.academic_years = academic_years

    def __repr__(self) -> str:
        return f"id: {self.id}, name: {self.name}, acronym: {self.acronym}, academic_years: {self.academic_years}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Degree) and o.id == self.id


class Course:
    def __init__(self, id: str, name: str, acronym: str, academic_term: str):
        self.id = id
        self.name = name
        self.acronym = acronym
        self.academic_term = academic_term

    def __repr__(self) -> str:
        return f"id: {self.id}, name: {self.name}, acronym: {self.acronym}, academic_years: {self.academic_term}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Course) and o.id == self.id


class Student:
    def __init__(self, username: str):
        self.username = username
        self.tecnico_id = int(username[3:])

    def __repr__(self) -> str:
        return f"id: {self.username}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Student) and o.id == self.id
