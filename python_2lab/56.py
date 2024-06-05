from datetime import datetime
class Period(): # 56.1
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2

    def getSeconds(self): # 56.2
        time1_dt = datetime.strptime(self.time1, "%Y-%m-%d %H:%M:%S")
        time2_dt = datetime.strptime(self.time2, "%Y-%m-%d %H:%M:%S")
        diff = time1_dt - time2_dt
        return diff.total_seconds()

    def getMinutes(self): # 56.3
        return self.getSeconds() // 60

    def getHours(self): # 56.4
        return self.getMinutes() // 60

    def getDays(self): # 56.5
        return self.getHours() // 24

period = Period("2023-05-09 12:48:00", "2023-02-11 14:01:00")
print(period.getSeconds())
print(period.getMinutes())
print(period.getHours())
print(period.getDays())
