# from semesters.semesters import Semesters

class Student:
    
    def __init__(self, grade_book: str, group: str, full_name: str, position: int):
        self.grade_book: str = grade_book
        self.group: str = group
        self.full_name: str = full_name
        self.position: int = position
        # self.semesters: Semesters = Semesters(student=self)
        
    def __str__(self):
        outer_text: str = f"""Выбраны следующие параметры студента:
        1. ФИО: {self.full_name}
        1. Группа: {self.group}
        1. Зачетка: {self.grade_book}
        1. Номер в списке группы: {self.position}
        """
        
        return outer_text