class Employee():
    def __init__(self, name, salary): # 12.1 Передача свойств в конструктор класса
        self.name = name
        self.salary = salary

    def getName(self): # 12.2 Метод для вывода имени работника
        print(self.name)

    def getSalary(self): # 12.3 Метод для вывода зарплаты работника
        print(self.salary)

    def increaseSalary(self): # 12.4 Метод для увеличения зарплаты работника на 10%
        self.salary *= 1.1

worker = Employee("Bob", 25000)
worker.getName()
worker.getSalary()
worker.increaseSalary()
worker.getSalary()