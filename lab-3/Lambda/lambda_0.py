"""
# A lambda function is a small anonymous function.

# Note : A lambda function can take any number of arguments, but can only have one expression.
# Syntax :
lambda arguments : expression
"""


# ex : Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# Note : Lambda functions can take any number of arguments:
# ex: Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, 
and that argument will be multiplied with 
an unknown number:
"""

def myfunc(n):
  return lambda a : a * n

# Use that function definition to make a function
# that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))