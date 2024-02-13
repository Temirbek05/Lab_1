# Write a Python program to convert degree to radian.

import math

deg = int(input("Input degree: "))

def converter(degree):
    radian = (degree * math.pi)/180
    return round(radian, 6)

res = converter(deg)
print(f"Output degree: {res}")