# You are given list of numbers separated by spaces. 
# Write a function filter_prime which will take list of numbers as an agrument
# and returns only prime numbers from the list.

"""
a = input("Enter a list of numbers: ").split()
a = list(map(int, a))
x = lambda b : b > 1 and all(b % i != 0 for i in range(2, int(b**0.5) + 1))

res = list(filter(x, a))

print("Prime numbers in the list:", res)


-------

numbers = input("Enter a list of numbers separated by space: ").split()

numbers = list(map(int, numbers))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

prime_numbers = []

for num in numbers:
    # Initialize a boolean flag to indicate if the number is prime
    is_prime_num = True
    
    if is_prime(num):
        # If the number is prime, append it to the list of prime numbers
        prime_numbers.append(num)

print("Prime numbers in the list:", prime_numbers)

"""

def isPrime(num):
    if num < 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    prime = []
    for num in nums:
        if isPrime(num):
            prime.append(num)
    return prime

nums = list(map(int, input("Enter a list of numbers: ").split()))
prime = filter_prime(nums)
print("Prime numbers in the list:", prime)