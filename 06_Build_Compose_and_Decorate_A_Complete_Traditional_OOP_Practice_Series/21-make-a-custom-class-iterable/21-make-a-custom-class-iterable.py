#?21. Make a Custom Class Iterable
#?Assignment:
#?Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object #?iterable in a for-loop, counting down to 0.

class Countdown:
  def __init__(self, start) -> None:
    self.start = start
    self.current = start

  def __iter__(self):
    return self
  
  # ?Define the next method for iteration
  def __next__(self):
    if self.current < 0:
      raise StopIteration
    result =self.current
    self.current -=1
    return result
  
  # ?Test the iterable class

countdown = Countdown(5)
for num in countdown:
  print(num, end= " ")

