# Write a Python program to subtract five days from current date.

import datetime


x = datetime.datetime.now() - datetime.timedelta(days=5)
print(f"Current date: {datetime.datetime.now()}")

print(f"Five days ago: {x}")

