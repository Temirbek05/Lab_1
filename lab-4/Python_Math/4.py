# Write a Python program to calculate the area of a parallelogram.

length = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

def area(l, h):
    ar = l * h
    return ar

res = float(area(length, height))
print(f"Expected Output: {res}")