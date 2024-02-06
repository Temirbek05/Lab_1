# We have used the Student class to create an object named x.

# What is the correct syntax to execute the printname method of the object x?

class Person:
  def __init__(self, fname):
    self.firstn = fname

  def printname(self):
    print(self.firstn)

class Student(Person):
  pass

name = input("Enter your name: ")

x = Student(name)
x.printname()

