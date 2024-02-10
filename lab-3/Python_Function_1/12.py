# Define a functino histogram() that takes a list of integers
#  and prints a histogram to the screen. For example, histogram([4, 9, 7]) 
# should print the following:


numbers = list(map(int, input("Enter the list of the numbers: ").split()))

def histogram(nums):
    histo = []
    for num in nums:
        res = '*' * num 
        histo.append(res)
    return histo
    
res = histogram(numbers) 
for row in res:
    print(row)
    
