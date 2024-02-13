# # Write a Python program to calculate two date difference in seconds.

import datetime
import random

ran_days = random.randint(1, 30)
ran_min = random.randint(1, 60)
ran_seconds = random.randint(1, 60)

x1 = datetime.datetime.now()

x2 = x1 - datetime.timedelta(days=ran_days, minutes=ran_min, seconds=ran_seconds)

# x2_future = x1 + x2

res = abs(x2 - x1)

total_seconds_diff = res.total_seconds()

print("Difference in seconds:", total_seconds_diff)
print(f"Comparable date: {x2.strftime("%X")}")
