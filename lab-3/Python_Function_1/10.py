# Write a Python function that takes a list 
# and returns a new list with unique elements of the first list. 
# Note: don't use collection set.

nums = list(map(int, input("Enter the list of numbers: ").split()))

def unique(kerek):
    kerek.sort()
    new_list = []
    for i in range(len(kerek) - 1):
        if kerek[i] != kerek[i+1]:
            new_list.append(kerek[i])
        else:
            continue
    new_list.append(kerek[-1])
    return new_list

jana = unique(nums)
print(f"Here is the new list consisting only unique: {jana}")

