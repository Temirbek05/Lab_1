# Write a Python program to calculate the area of a trapezoid.

Heihgt = int(input("Enter the height: "))
Base_1 = int(input("Base, first value: "))
Base_2 = int(input("Base, second value: "))

def area(h, b1, b2):
    ar = ((b1 + b2)*h)/2
    return ar

res = area(Heihgt, Base_1, Base_2)
print(f"Expected Output: {res}")