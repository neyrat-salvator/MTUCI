# from semesters.semesters import Semesters

class Student:
    
    def __init__(self, grade_book: str, group: str, full_name: str, position: int):
        self.grade_book: str = grade_book
        self.group: str = group
        self.full_name: str = full_name
        self.position: int = position
        self.variants_5: list = []
        # self.semesters: Semesters = Semesters(student=self)
        
    def __str__(self):
        outer_text: str = f"""Выбраны следующие параметры студента:
        1. ФИО: {self.full_name}
        2. Группа: {self.group}
        3. Зачетка: {self.grade_book}
        4. Номер в списке группы: {self.position}
        """
        if len(self.variants_5) != 0:
            outer_text += f'5. 5 Вариантов для вопросов: {self.variants_5}'
        
        return outer_text
    
    def get_5_vars(self):
        coefficient_list: list = [0, 5, 10, 15, 20]
        outer_variants: list = []
        for item in coefficient_list:
            current_variant: int = self.position + item
            outer_variants.append(current_variant)
        self.variants_5 = outer_variants
        
        return outer_variants