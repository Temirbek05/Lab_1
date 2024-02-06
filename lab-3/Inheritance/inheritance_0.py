"""Python Inheritance

Inheritance allows us to define a class
that inherits all the methods and properties from another class.

Parent class is the class being inherited from, 
also called base class.

Child class is the class that inherits from another class, 
also called derived class.
"""


# Creating a Parent class :

class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
# Create a class named Child, which will inherit the properties
# and methods from the Person class:

class Child(Parent):
    def address(self, job, home):
        self.job_address = job
        self.home_address = home 

# Use the Person class to create an object, 
# and then execute the printname method:

y = Child("Temirbek", "Boltay")
y.address("Office", "Los Angeles")
y.printname()

print(f"\nAddress:\nJob Adress is: {y.job_address}\nHome Adress: {y.home_address}")

# ex: Use the super() Function 
# Python also has a super() function that will make the child
# class inherit all the methods and properties from its parent:

class Person():
    def __init__(self, fname, lname):
      self.firstn = fname
      self.lastn = lname
      
    def printname(self):
       print(self.firstn, self.lastn)
        
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
print("\n")
x = Student("Mike", "Olsen")
x.printname()
 
