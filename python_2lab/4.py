class Employee():
    pass

worker1 = Employee() #4.1 Создание экземпляра класса
worker2 = Employee() #4.1 Создание экземпляра класса
worker3 = Employee() #4.1 Создание экземпляра класса

# 4.2 Запись свойств каждому работнику
worker1.name = 'Bob'
worker1.salary = 19000

worker2.name = 'Mike'
worker2.salary = 25000

worker3.name = 'Saul'
worker3.salary = 500000

print(worker1.salary + worker2.salary + worker3.salary) # 4.3 Вывод суммы зарплат