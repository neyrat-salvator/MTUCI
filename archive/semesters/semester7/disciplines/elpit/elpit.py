from student import Student


class Elpit:
    
    def __init__(self, student: Student):
        self.discipline_name: str = 'Электропитание устройств и систем инфокоммуникаций'
        self.variant_algorithm(grade_book=student.grade_book)
        
    def __str__(self):
        outer_text: str = f'Выбраны следующие параметры для дисциплины "{self.discipline_name}":\n'
        print(f'')
        for attr_key, attr_value in vars(self).items():
            if attr_key == 'discipline_name':
                continue
            outer_text += f'\n{attr_key}: {attr_value}'
        
        return outer_text
        
    def variant_algorithm(self, grade_book: str):
        self.variant_first_attr: int = int(grade_book[-2])
        self.variant_second_attr: int = int(grade_book[-1])