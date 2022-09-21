# polymorphism (many forms)

# method overloading

class methodoverload():
  def display(self,a=None,b=None,c=None):
    print(a,b,c)
obj = methodoverload()
obj.display(1,2,3)
obj.display(1,2)
obj.display(1)
obj.display()