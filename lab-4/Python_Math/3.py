# Write a Python program to calculate the area of regular polygon.
import math
sides = int(input("Input number of sides: "))
length = int(input("Input length of a sides: "))

def area_polygon(s, l):
        ar = (s * l**2) / (4 * math.tan(math.pi / s))
        return int(ar)

res = area_polygon(sides, length)
print(f"The area of the polygon is: {res}")