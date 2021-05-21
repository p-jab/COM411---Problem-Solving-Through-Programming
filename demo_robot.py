class Robot:
  # A class attribute
  laws = "Protect, Obey and Survive"

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # a class method
  @classmethod
  def assemble(cls):
    return cls("Assembled Robot" + input())

  # An initialiser (special instance method)
  def __init__(self, name = "Robot"):

    # An instance attribute
    self.name = name
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")


Robot.the_laws()
R1 = Robot()
R2 = Robot("Beep")
R3 = Robot.assemble()

R1.display()
R2.display()
R3.display()