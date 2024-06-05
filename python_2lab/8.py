class Student():
    name = None
    surname = None
    def toUpper(self, str): # 8.2 Создание вспомогательного метода, который будет получать первый символ строки и делать его заглавным.
        return str.capitalize()
    def getInitials(self): # 8.3 Создание метода, который вернет инициалы студента, то есть первые буквы его имени и фамилии.
        return f"{self.name[0]}. {self.surname[0]}."

student = Student()
student.name = "Bob" # 8.1 Запись свойства name
student.surname = "Brown" # 8.1 Запись свойства surname