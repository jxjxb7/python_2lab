from datetime import datetime
class Month(): # 59.1
    def __init__(self, date):
        self.date = date
        self.date = datetime.strptime(self.date, "%m")
    def getMonth(self): # 59.2
        return self.date.month
    def getMonthName(self): # 59.3
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

    def getLastDay(self): # 59.4
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[self.date.month - 1]
    def getFirstDayOfWeek(self): # 59.5
        days_in_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        first_day = 1
        return days_in_week[(first_day - 1) % 7]

    def getLastDayOfWeek(self): # 59.6
        days_in_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        last_day = self.getLastDay()
        return days_in_week[(last_day - 1) % 7]

month = Month("6")
print(month.getMonth())
print(month.getMonthName())
print(month.getLastDay())
print(month.getFirstDayOfWeek())
print(month.getLastDayOfWeek())