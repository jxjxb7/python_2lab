class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    fuel_type = None # 1.1 Создание свойства
    oil = None # 1.1 Создание свойства

    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass

    def stop(self):
        # Команда остановиться:
        pass
    def getColor(self): # 1.2 Создание функции вывода информации
        print(self.color)
    def getFuel(self): # 1.2 Создание функции вывода информации
        print(self.fuel)
    def getFuelType(self): # 1.2 Создание функции вывода информации
        print(self.fuel_type)
    def getOil(self): # 1.2 Создание функции вывода информации
        print(self.oil)

myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.fuel_type = "Petrol" # 1.1 Установка значения
myCar.oil = 20 # 1.1 Установка значения

myCar.go()
myCar.turn()
myCar.stop()

myCar2 = Car() # 1.3 Создание объекта класса
myCar2.color = 'Black'
myCar2.fuel = 100
myCar2.fuel_type = "Diezel"
myCar2.oil = 10
myCar2.getColor() # 1.3 Вывод данных
myCar2.getFuel() # 1.3 Вывод данных
myCar2.getFuelType() # 1.3 Вывод данных
myCar2.getOil() # 1.3 Вывод данных