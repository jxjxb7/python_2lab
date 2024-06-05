class User:
    # 38.1 Код с использованием защищенного свойства
    _name = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def setName(self, name):
        if len(name) > 0:
            super().setName(name)

worker = Employee()
worker.setName("Bob")
print(worker.getName())