# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.

nums =  int(input("Enter the number: "))


def kira(num):
    for i in range(num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

kerek = kira(nums)
ker = ', '.join(map(str, kerek))

print(f"Result: {ker}")


