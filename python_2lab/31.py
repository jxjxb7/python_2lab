class Employee():
    __name = None
    __salary = None
    __surname = None
    __age = None
    def __init__(self, name, salary, surname, age):
        self.__name = name
        self.__salary = salary
        self.__surname = surname
        self.__age = age

    def getName(self): # 25.2
        return self.__name

    def getSalary(self): # 25.1
        return str(self.__salary) + "$"

    def getSurname(self): # 25.3
        return self.__surname

    def getAge(self):
        return self.__age
    def setName(self, name): # 25.2
        self.__name = name

    def setSalary(self, salary): # 25.1
        self.__salary = salary

    def setSurname(self, surname): # 25.3
        self.__surname = surname
    def setAge(self, age): #
        self.__age = age

class User(Employee):
    def setAge(self, age): # 31.2
        if (18 < age < 65):
            self.__age = age
        else:
            raise Exception("age is incorrect!")
user = User("Bob", 25000, "White", 18)
user.setAge(25)
print(user.getAge())
