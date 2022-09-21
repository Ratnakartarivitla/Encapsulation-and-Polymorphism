# method overriding

class methodoverriding():
  def display(self):
    print("this is display one")
class method(methodoverriding):
  def display(self):
    print("this is dispaly in child")
    super().display()
obj = method()
obj.display()