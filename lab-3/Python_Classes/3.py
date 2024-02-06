# Define a class named Rectangle which inherits from Shape class from task 
# 2. Class instance can be constructed by a length and width. The Rectangle class
# has a method which can compute the area.

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.arg1 = length
        self.arg2 = width
        
    def area(self):
        return self.arg1 * self.arg2
    
lengthg = float(input("Enter the length of Rectangle: "))
widthg = float(input("Enter the width of Rectangle: "))
res = Rectangle(lengthg, widthg)

print("The area of the Rectangle is :", res.area())

