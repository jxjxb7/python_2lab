class User:
    age = None
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('need age more 0')

class Employee(User):
    def setAge(self, age):
        if age <= 120:
            super().setAge(age)
        else:
            raise Exception('need age less 120')

worker = Employee()
worker.setAge(5)
print(worker.age)
