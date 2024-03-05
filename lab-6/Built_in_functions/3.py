# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

txt = input("Enter a string: ")
kerek = txt[::-1]

d = False
for i in kerek:
    if i.isalnum():
        d = True
    else:
        d = False 
if kerek == txt and d:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
    