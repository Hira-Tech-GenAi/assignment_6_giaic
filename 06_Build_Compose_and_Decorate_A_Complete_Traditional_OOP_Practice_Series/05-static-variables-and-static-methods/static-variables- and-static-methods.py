#?Assignment:
#?Create a class MathUtils with a static method add(a, b) that returns the sum. #?No class or instance variables should be used.

class MathUtils:
  @staticmethod
  def add_two(a:int, b:int) -> int:
    return a + b

result= MathUtils.add_two(2,4)
print(f"sum : {result}")
