#?20. Creating a Custom Exception
#?Assignment:
#?Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18 Handle it with try...except.


class InvalidAgeError:
  pass

def check_age(age):
  if age < 18 :
    raise InvalidAgeError("Age must be at least 18")
  print(f"Age {age}is invalid")

try:
  check_age(14)

except:
  raise
