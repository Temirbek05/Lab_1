# Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the 
# shape where Shape's area is 0 by default.

class Shape:
    def area(self):
        return 0
class Square:
    def __init__(self, length):
        self.arg = length
        
    def area(self):
        return self.arg * self.arg
    
lengthg = float(input("Enter the length of square: "))
res = Square(lengthg)

print("The area of the square is :", res.area())

