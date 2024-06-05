class Employee():
    # 13.1 Создание приватных свойств
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age): # 13.2 Передача свойств в конструктор класса
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getData(self):
        print(self.__name)
        print(self.__salary)
        print(self.__age)

worker = Employee("Bob", 25000, 18)
worker.getData()