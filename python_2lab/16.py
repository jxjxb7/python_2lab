class Employee():
    # 16.1 Создание приватных свойств
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age): # 16.2 Передача свойств в конструктор класса
        self.__name = name
        self.__salary = salary
        self.__age = age

    # 16.3 Создание геттеров для свойств
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

worker = Employee("Bob", 25000, 18)
print(worker.getName())
print(worker.getSalary())
print(worker.getAge())