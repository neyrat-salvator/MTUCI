from student import Student
from elpit import Elpit


if __name__ == '__main__':
    grade_book: str = '3БСТ22384'
    group: str = 'БСТ2257'
    full_name: str = 'Юрцук Константин Сергеевич'
    position: int = 28
    
    student = Student(position=position, grade_book=grade_book, group=group, full_name=full_name)
    elpit = Elpit(student=student)
    print(student)
    print(elpit)
    
    True