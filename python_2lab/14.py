class Employee:
  def __init__(self,name, salary):
    self.name = name
    self.salary = salary

  def getSalary(self):
    return self.__addSign(self.salary) # 14.1 Использование приватного метода


  def __addSign(self,num): # 14.1 Создание приватного метода
	return num + '$'