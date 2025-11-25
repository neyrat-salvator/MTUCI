from student import Student
from semester7.semester7 import Semester7


class Semesters:
    
    def __init__(self, student: Student):
        self.semester7: Semester7 = Semester7(student=student)