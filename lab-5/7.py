# Write a python program to convert snake case string to camel case string.

import re

text = input("Enter a snake case string: ")

x = re.sub(r"_([a-z])", lambda res: res.group(1).upper(), text)
x = x[0].upper() + x[1:]

print(f"Converted string: {x}")


        
