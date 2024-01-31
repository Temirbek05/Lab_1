# Dictionaries are used to store data values in key:value pairs.

# Note : ordered*, changeable, do not allow duplicates.


# to covert dictionary by using dict() constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
for i in thisdict:
    print(i + ":", thisdict[i])

# Get the value of the "model" key:
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# or

x = thisdict.get("model")

# (*) The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys() # also value
print(x)

# (*) The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()
print(x)

# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

'''
(*) Nested Dictionaries
'''

# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for child_key in myfamily :
    print(child_key + ":", sep = '\n')
    for attribute_key in myfamily[child_key]:
        print(attribute_key + ":", myfamily[child_key][attribute_key])





