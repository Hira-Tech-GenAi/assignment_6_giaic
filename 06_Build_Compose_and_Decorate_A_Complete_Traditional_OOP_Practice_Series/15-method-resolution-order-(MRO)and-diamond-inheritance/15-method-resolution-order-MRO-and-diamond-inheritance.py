#?15. Method Resolution Order (MRO) and Diamond Inheritance
#?Assignment:
#?Create four classes:
#?
#?A with a method show(),
#?
#?B and C that inherit from A and override show(),
#?
#?D that inherits from both B and C.
#?
#?Create an object of D and call show() to observe MRO.

class A:
  def show(self):
    print("Show from A")

class B(A):
  
  def show(self):
    print("Show from B")
  




class C(A):
  
  def show(self):
    print("Show from C")

class D(B,C):
  pass

d= D()
d.show()  #? Output: Show from B (follows MRO: D -> B -> C -> A)
print(D.__mro__)  #? Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

