# Write a function that accepts string from user, return
# a sentence with the words reversed. We are ready -> ready are We


stringg = input("Enter a string you want to reverse: ").split()

def Reverse(string): 
    string.reverse()
    return " ".join(string)

res = Reverse(stringg)
print(f"reversed string: {res}")

