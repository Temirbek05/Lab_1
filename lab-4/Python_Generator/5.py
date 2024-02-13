# Implement a generator that returns all numbers from (n) down to 0.

n = int(input("Enter the number: "))

def all(num):
    for i in range(num, -1, -1):
        yield i 
    
res = all(n)
ker = ', '.join(map(str, res))
print(ker)
