#1. Using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values #via a constructor. Add a method display() that prints student details.

class Student:
  def __init__(self, name:str, marks:int):
    self.name:str = name
    self.marks:int = marks
  def display(self):
    return (f"Student Name{self.name}, Student Total Marks: {self.marks}")
  
student1 = Student("Hira", 900)  
print(student1.display())