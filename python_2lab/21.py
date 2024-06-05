class Student:
    pass


class Employee:
    pass


employee = Employee()
print(isinstance(employee, Employee)) # True т.к. правильный класс
print(isinstance(employee, Student)) # False т.к. неправильный класс