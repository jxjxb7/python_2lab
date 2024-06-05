from datetime import datetime
class Zate(): # 57.1
    def __init__(self, date):
        self.date = date
        self.date = datetime.strptime(self.date, "%Y-%m-%d")

    def getYear(self):
        return self.date.year
    def getMonth(self): # 57.3
        return self.date.month

    def getDay(self): # 57.4
        return self.date.day

    def getWeekday(self):# 57.5
        return self.date.weekday()

    def getWeekdayName(self): # 57.6
        weekdayNames = {1 : "Понедельник", 2 : "Вторник", 3 : "Среда", 4 : "Четверг", 5 : "Пятница", 6 : "Суббота", 7 : "Воскресенье"}
        return weekdayNames[self.getWeekday()]

    def getMonthName(self): # 57.7
        monthNames = {
            1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь'}
        return monthNames[self.getMonth()]

zate = Zate("2023-10-11")
print(zate.getYear())
print(zate.getMonth())
print(zate.getDay())
print(zate.getWeekday())
print(zate.getWeekdayName())
print(zate.getMonthName())