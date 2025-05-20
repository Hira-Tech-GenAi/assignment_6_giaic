#?13. Composition
#?Assignment:
#?Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during #?initialization. Access a method of the Engine class via the Car class.

#? Define the Engine class
class Engine:
  def start(self):
    print("engine started")

#? Define the Car class using composition
class Car(Engine):

  def __init__(self, engine):#? Composition: Car has an Engine
    self.engine = engine
  def start_car(self):# Call Engine's method
    self.engine.start()


# Test composition
engine = Engine()
car = Car(engine)
car.start_car()

