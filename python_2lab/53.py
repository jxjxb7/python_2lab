class Circle(): # 53.1
    __radius = None
    def __init__(self, radius): # 53.2
        self.__radius = radius

    def getSquare(self): # 53.3
        return 3.14 * self.__radius ** 2

    def getCircumferenceLength(self): # 53.4
        return 2 * 3.14 * self.__radius

circle = Circle(5)

print(circle.getSquare())
print(circle.getCircumferenceLength())
