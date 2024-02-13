# Write a Python program to drop microseconds from datetime.

import datetime

x = datetime.datetime.now().strftime("%f")
print(x)

