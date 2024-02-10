# Given a list of ints, return True if the 
# array contains a 3 next to a 3 somewhere.


list_integers = list(map(int, input("Enter the list of numbers: ").split()))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

res = has_33(list_integers)
print(res)
