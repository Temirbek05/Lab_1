# Create a generator that generates the squares of numbers up to some number N.

def gen(nums):
    for num in nums:
        yield num ** 2

list_num = list(map(int, input("Enter the list of numbers: ").split()))
squares_generator = gen(list_num)

res = [square for square in squares_generator]
print(res)
