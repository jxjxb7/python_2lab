class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def getSurn(self):
        return self.surname

class Employee(User): # 33.1
    def __init__(self, name, surname, age, salary): # 33.2
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    # 33.3
    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary

worker = Employee("Bob", "Smith", 25, 35000)

