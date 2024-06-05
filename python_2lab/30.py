class User():
    def sayHi(self):
        print("Hi, I'm user!")
class Employee(User):
    __name = None
    __salary = None
    __surname = None
    def __init__(self, name, salary, surname):
        self.__name = name
        self.__salary = salary
        self.__surname = surname

    def getName(self): # 25.2
        return self.__name

    def getSalary(self): # 25.1
        return str(self.__salary) + "$"

    def getSurname(self): # 25.3
        return self.__surname
    def setName(self, name): # 25.2
        self.__name = name

    def setSalary(self, salary): # 25.1
        self.__salary = salary

    def setSurname(self, surname): # 25.3
        self.__surname = surname

worker = Employee("Bob", 25000, "White")

# 25.4
worker.setName("John")
worker.setSalary(12500)
worker.setSurname("Black")
print(worker.getName())
print(worker.getSalary())
print(worker.getSurname())
worker.sayHi()