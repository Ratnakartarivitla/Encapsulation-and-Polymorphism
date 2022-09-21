# Encapsulation

# Access Specifiers
# Private - _ , protected - __ , Public - it is normal
class GFather():
  def __init__(self,a):
    self._b = a
    print(self._b)
class Parent(GFather):
  def display(self):
    print(self._b)
class Child(Parent):
  def display2(self):
    print(self._b)

obj = Child(2)
obj.display()
obj.display2()