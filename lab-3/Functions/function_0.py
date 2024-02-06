# examples of functions :

# 1. to create function :

def my_function():
    print("Hello from my function")

# 2. to execute :

name = input("Enter your name ")
def my_function(name):
    return name +  " Boltay"
res = my_function(name)
print(res)

# 3. call any argument among many : 

def my_function(arg1, arg2):
    print(arg1)

# 4. If the number of arguments is unknown, add a * before the parameter name:

def my_funct(*kids):
    return kids[2]
kids = ("Tima", "Nurik", "Rustam")

# 5.  You can also send arguments with the key = value syntax.

def my_funct(kid1, kid2, kid3):
    print("The youngest kid is " + kid3)
my_funct(kid1 = "Any", kid2 = "Tobias", kid3 = "Emil")

# 6. If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_f(**kid):
    print("His last name is " + kid["lname"])
my_f(fname = "Tobias", lname = "Refsnaes")

# 7. If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 8. Passing a List as an Argument

fruits = ["apple", "banana", "cherry"]
i = len(fruits)
def my_function(food):
    global i
    while i != 0:
        i-=1
        print(fruits[i])

my_function(fruits)

# 9. Keyword-Only Arguments

def my_function(*, x):
    print(x)
my_function(x = 3)


"""
def my_function(x, /):  --< slash at the end
  print(x)

my_function(3). ---

and 

def my_function(*, x): --< star at the beginning
  print(x)

my_function(x = 3). ---

"""

# 10. Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

""" output :
Recursion Example Results
1
3
6
10
15
21
"""
    
