"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""

# 0.1. creating a class

class MyClass:
    x = 5
# 0.2. creating object
p1 = MyClass()
print(p1.x)

# 1. The _init_() Function

"""
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary 
to do when the object is being created:
"""

# ex :
 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name + " is " + str(p1.age))


"""
# The __str__() Function
The __str__() function controls what should be returned 
when the class object is represented as a string.

If the __str__() function is not set, 
the string representation of the object is returned:
"""

# ex : 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

"""
Object Methods
Objects can also contain methods. 
Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
"""

# ex : Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print("My name is ", p1.name, " is ", p1.age)

"""
The self Parameter
The self parameter is a reference to 
the current instance of the class, and is used to access
variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:
"""

# Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# ex : Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    
  def __str__(mysillyobject):
    return f"{mysillyobject.name}({mysillyobject.age})"

p1 = Person("John", 36)
p1.myfunc()

print(p1.name, "You are always welcome to ask anything as you are ", p1.age, "years old")

# You can modify properties on objects like this:

# ex :
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Mike", 30) 
p1.age = 40

print("Hey, ", p1.name, "it's me,", p2.name)  

print("Oh,", p1.name, "it's been 4 years since we met last time, apparently now you are turning", p1.age, "this year")

