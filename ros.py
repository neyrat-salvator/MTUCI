from student import Student
from ros_tasks.task_resolve import *


class ROS:
    
    def __init__(self, student: Student):
        self.discipline_name: str = 'Распределенные операционные системы'
        self.student: Student = student
        
    def __str__(self):
        outer_text: str = f"""Выбраны следующие параметры дисциплины:
        1. Наименование дисциплины: {self.discipline_name}
        """
        
        return outer_text
    
    def resolve_task1(self):
        max_variant: int = 25
        outer_value: int = self.student.position % max_variant
        
        return ROSTask1(variant=outer_value)
    
    def resolve_task2(self):
        max_variant: int = 25
        outer_value: int = self.student.position % max_variant
        
        return ROSTask2(variant=outer_value)