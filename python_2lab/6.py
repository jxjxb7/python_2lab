class Employee():
    def test_method(self, name, salary): # 6.1 Передача параметров в тестовый метод
        return f"Работник {name} имеет зарплату {salary}"

worker = Employee()
print(worker.test_method("john", 19000))