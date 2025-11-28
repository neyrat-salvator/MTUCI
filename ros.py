from student import Student
from ros_tasks.task_resolve import *


class ROS:
    
    def __init__(self, student: Student):
        self.discipline_name: str = 'Распределенные операционные системы'
        self.student: Student = student
        self.max_variant: int = 25
        self.current_variant: int = self.student.position % self.max_variant
        self.task1: ROSTask1 = ROSTask1(variant=self.current_variant)
        self.task2: ROSTask2 = ROSTask2(variant=self.current_variant)
        self.task3: ROSTask3 = ROSTask3(variant=self.current_variant)
        self.task4: ROSTask4 = ROSTask4(variant=self.current_variant)
        
    def __str__(self):
        outer_text: str = f"""Выбраны следующие параметры дисциплины:
        1. Наименование дисциплины: {self.discipline_name}
        {self.task1}
        {self.task2}
        {self.task3}
        {self.task4}
        """
        
        return outer_text