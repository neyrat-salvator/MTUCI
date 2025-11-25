from student import Student
from elpit.elpit import Elpit


class Disciplines:
    
    def __init__(self, student: Student):
        self.elpit: Elpit = Elpit(student=student)