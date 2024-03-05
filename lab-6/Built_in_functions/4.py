# Write a Python program that invoke square root function after specific milliseconds

# Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858


import time 

num = int(input("Enter the number: "))
milsec = int(input("Enter the delay time: "))
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
print(f"Square root of {num} after {milsec} miliseconds is {sqrt}")
