# rule : A set is a collection which is unordered, unchangeable*, and unindexed.

# to create a Set 

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# (*)Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

# Add elements from tropical into thisset:

"""
To add items from another set into the current set, use the update() method.
"""

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

"""
To remove an item in a set, use the remove(), or the discard() method.

"""
#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

"""
Remove a random item by using the pop() method:

"""

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)

print(thisset)

# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

"""
Note: Both union() and update() will exclude any duplicate items.
"""

# Note: The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Note: The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Note: The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

