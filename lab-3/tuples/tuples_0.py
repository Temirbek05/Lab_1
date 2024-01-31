# reules (A tuple is a collection which is ordered and unchangeable + allow duplicates)

""""
1. To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
ex : 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

2. Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

3. since tuple is not changable, we can convert it to list :
ex :
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

4. in Python we can extract the values back into variables - > "unpacking"
ex : 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

5. Using Asterisk * (Assign the rest of the values as a list called "red":)
ex : 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

6. 
"""

# ex : (for loop tuples)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# or 

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# ex : (while loop tuples)
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

"""
Method	| Description
count()	-- Returns the number of times a specified value occurs in a tuple
index()	-- Searches the tuple for a specified value and returns the position of where it was found

"""

# (*) Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# we can also Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)