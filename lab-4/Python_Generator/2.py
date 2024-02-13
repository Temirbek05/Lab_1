# # Write a program using generator to print the even
# # numbers between 0 and n in comma separated form where n is input from console.


n = int(input("Enter the nummber: "))

def eventek(nums):
    for i in range(nums + 1):
        if i % 2 == 0:
            yield i

res = eventek(n)
ker = ', '.join(map(str, res))
print(f"Even numbers between 0 and {n}: {ker}")
