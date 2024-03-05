# # Write a Python program to split a string at uppercase letters.

import re

text = input("Enter a string: ")
x = re.sub(r"([A-Z])", lambda kerek: " " + kerek.group(1), text).split()

print(x)

# def split_at_uppercase(string):
#     substrings = []
#     start_index = 0

#     for i, char in enumerate(string):
#         if char.isupper():
#             if i > start_index:
#                 substrings.append(string[start_index:i])
#             start_index = i

#     if start_index < len(string):
#         substrings.append(string[start_index:])

#     return substrings

# result = split_at_uppercase(text)
# print(result)

