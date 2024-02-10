# Write a Python function that checks whether a word
# or phrase is palindrome or not. Note: A palindrome is word, 
# phrase, or sequence that reads the same backward as forward, e.g., madam

stringg = input("Enter the string: ")

def Check(string):
    string_ch = string
    string_ch = []
    x = len(stringg) - 1

    while x >= 0:
        string_ch.append(stringg[x])
        x -= 1
    
    result = "".join(string_ch)

    if result == string:
        return True
    return False

res = Check(stringg)
print(res)
