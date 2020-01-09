"""Создать сотрудника Mary, пользуясь классом
Employee и перенести его в другую программу,
используя модуль Pickle и файловую систему.
Узнать про + и - модуля Pickle."""
import pickle
class Employee:
  def __init__(self,name,phone,salary=10000):
    self.name = name
    self.phone = phone
    self.salary = salary
  def print_salary_info(self):
    print("Employee {} gets {} Rubles".format(self.name,self.salary))
  def add_salary(self,delta=5000):
    self.salary = self.salary+delta
  def add(self,other_empl):
    new_name = self.name + "&" + other_empl.name
    new_phone = str(round( (int(self.phone) + int(other_empl.phone))/2 ))
    new_salary = self.salary + other_empl.salary
    return Employee(new_name,new_phone,new_salary)
  __add__=add
  def delete(self):
    print(self.name+" is FIRED!!!")

E1 = Employee("Mary", 9055, 150000)
f = open('/home/varya/Documents/homework/E1.pickle', 'wb')
pickle.dump(E1, f)
f.close()