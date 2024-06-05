class Employee():
    name = None
    position = None
    department = None
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department
class User :
  name = None
  position = None
  department = None

  def __init__(self,name, position, department):
    self.name = name
    self.position = position
    self.department = department

worker = Employee("John", "Director", "Technical")

user = User("John", worker.position, worker.department)
print(user.name, user.position, user.department, sep="\n")