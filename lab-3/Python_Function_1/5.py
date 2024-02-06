# Write a function that accepts string from user and 
# print all permutations of that string.


from itertools import permutations
string = input()
def permu(string):
    return permutations(string)

st = list(permu(string))

for per in st:
    print(''.join(per))

