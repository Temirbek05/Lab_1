# Write a program which can filter prime numbers in a list by using filter function.
# Note: Use lambda to define anonymous functions.

a = input("Enter a list of numbers: ").split()
a = list(map(int, a))
x = lambda b : b > 1 and all(b % i != 0 for i in range(2, int(b**0.5) + 1))

res = list(filter(x, a))

print("Prime numbers in the list:", res)