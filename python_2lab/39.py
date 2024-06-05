class User:
    def setName(self, name):
        if self.notEmpty(name):
            self.name = name

    def getName(self):
        return self.name

    def _notEmpty(self, stri):
        return len(stri) > 0


class Employee(User): # 39.1
    def setSurn(self, surname):
        if self._notEmpty(surname):
            self.surname = surname

    def getSurn(self):
        return self.surname
class Programmer(Employee): # 39.2
    # 39.4
    def setLanguage(self, language):
        self.language = language
    def getLanguage(self):
        return self.language
class Designer(Employee): # 39.3
    #39.4
    def setGraphicType(self, graphicType):
        self.graphicType = graphicType
    def getGraphicType(self):
        return self.graphicType


worker1 = Programmer()
worker1.setLanguage("Python")
print(worker1.getLanguage())

worker2 = Designer()
worker2.setGraphicType("Vector")
print(worker2.getGraphicType())
