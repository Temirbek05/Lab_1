# Write a Python program to print yesterday, today, tomorrow.

import datetime

d_y = datetime.datetime.now() - datetime.timedelta(days = 1)
d_t = datetime.datetime.now() + datetime.timedelta(days = 1)

print(f"Yesterday was: {d_y.strftime("%x")}")
print(f"Today: {datetime.datetime.now().strftime("%x")}")
print(f"Tomorrow will be: {d_t.strftime("%x")}")