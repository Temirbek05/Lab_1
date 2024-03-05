# Write a Python program to insert spaces between words starting with capital letters.

# import re

text = input("Enter a string: ")
# x = re.sub(r"([A-Z])", lambda kerek: " " + kerek.group(1), text)

# print(x)


result = ""

for i, char in enumerate(text):
    if char.isupper() and i != 0:
        result += " " + char
    else:
        result += char

print(result)
