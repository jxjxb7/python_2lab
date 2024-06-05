class Employee():
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return str(self.__salary) + "$"

    def getAge(self):
        return self.__age
    # 17.1 Добавление сеттеров свойств
    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        if (0 < age < 120):
            self.__age = age
        else:
            raise Exception("age is incorrect!")

worker = Employee("Bob", 25000, 18)
worker.setName("Joshua")
worker.setSalary(1000)
worker.setAge(29)
print(worker.getName())
print(worker.getSalary())
print(worker.getAge())