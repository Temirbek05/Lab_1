# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# 1. Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# 2. Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
  
# 3. Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# 4. Using the range() function: (not including 6)

for x in range(6):
  print(x)

# 5. Using the start parameter: (Increment the sequence with 3 (default is 1):)

for x in range(2, 6):
  print(x)

# 6. Break the loop when x is 3, and see what happens with the else block:


  for x in range(6):
    if x == 3: break
  print(x)
else:
  print("Finally finished!")


# 7.  Print each adjective for every fruit:
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
