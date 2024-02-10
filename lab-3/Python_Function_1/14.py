# Create a python file and import some of the functions 
# from the above 13 tasks and try to use them.

# 10 # 

nums = list(map(int, input("Enter the list of numbers: ").split()))

def unique(kerek):
    seen = []
    new_list = []
    for num in kerek:
        if num not in seen:
            new_list.append(num)
            seen.append(num)
    return new_list

jana = unique(nums)
print(f"Here is the new list consisting only unique: {jana}")
