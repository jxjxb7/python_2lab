class Employee:
  __name = None

  def __init__(self,name):
    self.__name = name

emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 == emp2)
# Результат сравнения False, так как сравниваются переменные, содержащие ссылку на разные объекты