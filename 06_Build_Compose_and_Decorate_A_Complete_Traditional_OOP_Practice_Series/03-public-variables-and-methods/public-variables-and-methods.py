#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the #class and access both from outside the class.

class Car:
  # Public variable
  brand = "Toyota"

  # Public method to simulate starting the car
  def start(self) -> None:
    print(f"{ self.brand} is starting.")

car = Car()
print(car.brand)
car.start()

#Har Car ka brand by default "Toyota" hoga.