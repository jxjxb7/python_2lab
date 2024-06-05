import re

class Validator(): # 22.1 Создание класса Validator
    def isEmail(self, email): # 22.2
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.search(pattern, email):
            print("Корректный email")
        else:
            print("Некорректный email")

    def isDomain(self, domain): # 22.3
        pattern = r'^[a-zA-Z0-9.-]+$'
        if re.search(pattern, domain):
            print("Корректный domain")
        else:
            print("Некорректный domain")

    def isNumber(self, numbers): # 22.4
        if numbers.isdigit():
            print("Только цифры")
        else:
            print("Не только цифры")



v = Validator()
v.isEmail("example@gmail.com")
v.isDomain("example.com")
v.isNumber("134234")