class Employee():
    name = None
    salary = None
    age = None
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

workers = [Employee("Dave", 25000, 19), Employee("Bob", 18000, 18), Employee("Nick", 100000, 25)] # 24.1

for worker in workers: # 24.2
    print(worker.name, worker.salary)
