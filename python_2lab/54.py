class Rectangle(): # 54.1
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getSquare(self): # 54.2
        return self.width * self.height

    def getPerimeter(self): # 54.3
        return 2 * self.width + 2 * self.height

    def getRatio(self): # 54.4
        return self.getSquare() / self.getPerimeter()

rectangle = Rectangle(10, 5)
print(rectangle.getSquare())
print(rectangle.getPerimeter())
print(rectangle.getRatio())