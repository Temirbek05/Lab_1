# Write a Python program with builtin function that accepts a string and calculate the 
# number of upper case letters and lower case letters



def counter(string):
    cntup = sum(1 for char in string if char.isupper())
    cntlow = sum(1 for char in string if char.islower())
    return cntup, cntlow

st = input("Enter a string: ")
cnt_up, cnt_low = counter(st)

print(f"There are {cnt_up} upper case letters and {cnt_low} lower case letters")
