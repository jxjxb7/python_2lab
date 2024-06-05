class Employee():
    name = None # 7.1 Создание свойств
    salary = None # 7.1 Создание свойств
    def getName(self): # 7.2 Метод вывода имени
        print(self.name)
    def getSalary(self): # 7.3 Метод вывода зарплаты
        print(self.salary)

worker = Employee()
worker.name = "Bob"
worker.salary = 17000
print(worker.getName())
print(worker.getSalary())