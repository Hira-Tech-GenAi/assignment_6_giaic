#?14. Aggregation
#?Assignment:
#?Create a class Department and a class Employee. Use aggregation by having a Department object store a #?reference to an Employee object that exists independently of it.



class Employee:
  def __init__(self, name):
    self.name = name

  def display(self):
    print(f"Employee name: {self.name}")




#? Define the Department class using aggregation
class Department:
  def __init__(self, name, employee):# employee ka reference store karenge (Aggregation).
    self.name = name
    self.employee = employee

  def show_employee(self):# Aggregation: Department references Employee
    self.employee.display()

# Test aggregation
employee = Employee("hira")
dept = Department("HR", employee)
dept.show_employee()
print(dept.name)






