class User:
    __name = ''

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Employee(User):
    __name = ''
    def __init__(self):
        __name = self.getName()
    def setName(self, name):
        if (len(name) > 0):
            super().setName(name)

worker = Employee()
worker.setName("Bob")
print(worker.getName())