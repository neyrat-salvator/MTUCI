from student import Student
from disciplines.disciplines import Disciplines


class Semester7:
    
    def __init__(self, student: Student, position: int):
        self.semester_number: int = 7
        self.position: int = position
        self.disciplines: Disciplines = Disciplines(student=student)
    
    def __str__(self):
        outer_text: str = f'Выбраны следующие параметры для {self.semester_number} семестра:\n'
        for attr_key, attr_value in vars(self).items():
            if attr_key == 'semester_number':
                continue
            outer_text += f'\n{attr_key}: {attr_value}'
        
        return outer_text