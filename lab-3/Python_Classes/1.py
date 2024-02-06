# Define a class which has at least two methods: getString: to get a string from console 
# input printString: to print the string in upper case.

class printString:
  def __init__(getString):
    getString.string = input("Enter string you want to convert to uppercase: ")

  def convert(getString):
    getString.string = getString.string.upper()
    
  def __str__(getString):
    return getString.string
  
res = printString()
res.convert()
print(res)


