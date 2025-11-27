from student import Student
from elpit import Elpit
from ros import ROS
from ros_tasks.task_resolve import ROSTask1, ROSTask2


if __name__ == '__main__':
    grade_book: str = '3БСТ22384'
    group: str = 'БСТ2257'
    full_name: str = 'Юрцук Константин Сергеевич'
    # position: int = 28
    position: int = 23
    
    student = Student(position=position, grade_book=grade_book, group=group, full_name=full_name)
    ros: ROS = ROS(student=student)
    ros1: ROSTask1 = ros.resolve_task1()
    ros2: ROSTask2 = ros.resolve_task2()
    # elpit = Elpit(student=student)
    print(student)
    print(ros)
    print(ros1)
    print(ros2)
    # print(elpit)
    
    True