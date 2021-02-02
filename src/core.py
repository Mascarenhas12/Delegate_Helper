class Degree:
    def __init__(self, id: str, name: str, acronym: str, academic_years: list):
        self.id = id
        self.name = name
        self.acronym = acronym
        self.academic_years = academic_years

    def __str__(self) -> str:
        return self.acronym

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

    def __str__(self) -> str:
        return f"{self.acronym}, {self.name}"

    def __repr__(self) -> str:
        return f"id: {self.id}, name: {self.name}, acronym: {self.acronym}, academic_years: {self.academic_term}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Course) and o.id == self.id


class Student:
    def __init__(self, username: str, acronym):
        self.username = username
        self.degree_acronym = acronym

    def __str__(self) -> str:
        return f"{self.username}, {self.degree_acronym}"

    def __repr__(self) -> str:
        return f"id: {self.username}, degree_acronym: {self.degree_acronym}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Student) and o.username == self.username
