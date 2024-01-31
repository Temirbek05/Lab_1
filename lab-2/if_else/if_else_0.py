# examples

"""
(*) 
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""

# if statement

a = 33
b = 200
if b > a:
  print("b is greater than a")

"""
# without indentation is wrong
  
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
"""

# The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
    
a = 33
b = 200

if b > a:
  pass