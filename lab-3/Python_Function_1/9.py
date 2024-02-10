# Write a function that computes the volume of a 
# sphere given its radius

import math

num = int(input("Enter the radius of sphere: "))

def Volume(radius):
    val = 4/3 * math.pi * radius
    return val

res = int(Volume(num))
print(res)