class User():
    def sayHi(self):
        print("Hi, I'm user!")

class Employee(User): # 28.1
    pass

worker = Employee()
worker.sayHi()