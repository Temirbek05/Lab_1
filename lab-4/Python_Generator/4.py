# Implement a generator called squares to yield the square of
#  all numbers from (a) to (b). Test it with a "for" loop and print
# each of the yielded values.
import math

a = int(input("Enter starting point: "))
b = int(input("Enter final point: "))

def squares(ap, bp):
    for i in range(ap, bp + 1):
        ch = math.sqrt(i)
        if ch.is_integer():
            yield i

res = squares(a, b)

ker = ', '.join(map(str, res))
print(ker)
