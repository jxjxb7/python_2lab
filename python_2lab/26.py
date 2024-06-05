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
        return self.__salary

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

class EmployeesCollection(): # 25.1
    __employees = None
    def __init__(self):
        self.__employees = []

    def add(self, employee): # 25.2
        self.__employees.append(employee)

    def show(self): # 25.3
        for employee in self.__employees:
            print(employee.getName())

    def salarySum(self): #25.4
        sum = 0
        for employee in self.__employees:
            sum += employee.getSalary()
        return sum

    def salaryAvg(self): # 25.5
        return self.salarySum() / len(self.__employees)

employees = EmployeesCollection()

employees.add(Employee("John", 25000, 19))
employees.add(Employee("Bob", 45000, 22))

employees.show()

print(employees.salarySum())
print(employees.salaryAvg())