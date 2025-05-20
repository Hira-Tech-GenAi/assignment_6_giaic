#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
#
#a public variable name,
#
#a protected variable _salary, and
#
#a private variable __ssn.
#
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
  def __init__(self) -> None:
    self.name = "hira"
    self._salary =100000
    self.__ssn =123_00_466

user = Employee()
print(f"username: {user.name}")
print(f"user salary: {user._salary}")
#!print(f"user ssn: {user.ssn}")

try:
    print(user.__ssn)    # Raises AttributeError (private, not accessible)
except AttributeError:
    print("Cannot access private variable __ssn")