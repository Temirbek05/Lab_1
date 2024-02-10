# Write a function that takes in a list of integers and returns 
# True if it contains 007 in order

input_integers = list(map(int, input("Enter the list of numbers: ").split()))

def spy_game(nums):
    zero_cnt = 0
    seven_cnt = 0
    for i in nums:
        if i == 0:
            zero_cnt += 1

        elif i == 7 and zero_cnt >= 2:
            seven_cnt += 1
            return True
        
    return False

res = spy_game(input_integers)

print(res)