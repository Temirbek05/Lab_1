# Write a Python program to convert a given camel case string to snake case.

# Enter a CamelCase string: ThisIsCamelCase
# Snake case: this_is_camel_case


import re

text = input("Enter a camel case string: ")

x = re.sub(r"([A-Z])", lambda res: "_" + res.group(1).lower(), text)
x = x.lstrip("_") 

print(f"Converted string: {x}")