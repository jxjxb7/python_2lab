class Text(): # 55.1
    def __init__(self, text): # 55.1
        self.text = text

    def getLength(self): # 55.2
        return len(self.text)

    def getLettersCount(self): # 55.3
        counter = 0
        for s in self.text:
            if s.isalpha():
                counter += 1
        return counter
    def getSpacesCount(self): # 55.4
        counter = 0
        for s in self.text:
            if s == " ":
                counter += 1
        return counter

    def getLengthWithoutSpaces(self): # 55.5
        return self.getLength() - self.getSpacesCount()

    def getWords(self): # 55.6
        return self.text.split()

    def getSentences(self): # 55.7
        return self.text.split('.')


text = Text("Привет! 12345 ")
print(text.getLength())
print(text.getLettersCount())
print(text.getSpacesCount())
print(text.getLengthWithoutSpaces())
print(text.getWords())
print(text.getSentences())