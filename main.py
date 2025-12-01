from student import Student
from elpit import Elpit
from ros import ROS
from datetime import datetime


if __name__ == '__main__':
    start_date: datetime = datetime.now()
    text1: str = f"""{start_date} - Программа начала свою работу.
    Программа создана исключительно в научных интересах и позволяет сравнивать свои данные в задачах с вычислениями программы.
    Программа не пересылает введенные данные на сторонние ресурсы.
    """
    print(text1)
    
    # Значения для дебаггинга
    # debugging: bool = True
    # full_name: str = 'Юрцук Константин Сергеевич'
    # group: str = 'БСТ2257'
    # grade_book: str = '3БСТ22384'
    # position: int = 28
    
    # Значения для инициализации
    debugging: bool = False
    full_name: str = input('Введите ФИО полностью на русском языке: ')
    group: str = input('Введите группу полностью на русском языке: ')
    grade_book: str = input('Введите номер зачетки полностью на русском языке: ')
    position: int = int(input('Введите свой актуальный номер в списке: '))
    
    student = Student(position=position, grade_book=grade_book, group=group, full_name=full_name)
    student.get_5_vars()
    # ros: ROS = ROS(student=student)
    # elpit = Elpit(student=student)
    print(student)
    # print(ros)
    # print(elpit)
    end_date: datetime = datetime.now()
    date_diff: datetime = end_date-start_date
    text2: str = f"""{end_date} - Программа закончила свою работу.
    Время работы: {date_diff}
    Всё готово. Можно свободно копировать любые данные куда-угодно.
    Не нажимайте Ctrl+C без выделения текста, это закроет терминал.
    Но, конечно, вы можете запустить программу снова без трудностей :)
    """
    print(text2)
    if not debugging:
        input('Нажмите Enter для завершения программы...')
    
    # True