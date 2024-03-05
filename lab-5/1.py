# Write a Python program that matches a string 
# that has an 'a' followed by zero or more 'b''s.

import re

txt = input("Enter a string: ")
x = re.search("a.*b*$", txt)
if x:
    print("There is a macth")
else:
    print("No match")