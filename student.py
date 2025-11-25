# from semesters.semesters import Semesters

class Student:
    
    def __init__(self, grade_book: str, group: str, full_name: str, position: int):
        self.grade_book: str = grade_book
        self.group: str = group
        self.full_name: str = full_name
        self.position: int = position
        # self.semesters: Semesters = Semesters(student=self)
        
    def __str__(self):
        outer_text: str = 'Выбраны следующие параметры студента:\n'
        for attr_key, attr_value in vars(self).items():
            outer_text += f'\n{attr_key}: {attr_value}'
        
        return outer_text