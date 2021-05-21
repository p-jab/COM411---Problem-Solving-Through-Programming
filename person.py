#The class i.e. blueprint for my objects
class Person:

  #Class attribute -> constant, visible to all objects of the class
  MAX_ENERGY = 100
  #Initialiser (special instance method, invoked only once, at creation)
  @staticmethod
  def is_mature(age):
    if age > 18:
      return True
    else:
      return False
  
  def __init__(self, name, age = 0, weight = 10, energy = 100):
    #Instance attributes
      self.name = name
      self.age = age
      self.weight = weight
      if energy > 100:
        self.energy = Person.MAX_ENERGY
      else:
        self.energy = energy

  def hello(self):
    print(f"Hello, my name is {self.name}. I am {self.age} years old and I weight {self.weight}kg. Nice to meet you!")

  def grow(self):
    self.age += 1

  def eat(self, food, weight):
    self.weight += weight
    print(f"{self.name} have eaten {food} and now wights {self.weight}kg")
  

if __name__ == "__main__":

  Piotr = Person("Piotr", 66, 81, 65)
  Anca = Person("Anca", 18)
  Mihai = Person("Mihai")
  Tim = Person("Tim", weight = 87)

  Anca.hello()
  Tim.hello()
  Piotr.hello()
  Mihai.hello()

  Piotr.grow()
  Piotr.hello()

  Tim.eat("Lasagne", 2)
  Tim.hello()