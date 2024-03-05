# Write a Python program that matches a string 
# that has an 'a' followed by two to three 'b'.

import re 

txt = input("Enter a string: ")
pattern = re.compile(r"ab{2,3}")
if pattern.search(txt):
    print("There is a macth!")
else:
    print("No match!")
