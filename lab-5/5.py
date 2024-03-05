"""
# Original matrix A
A = [[1, 2, 3],
     [4, 5, 6]]

# Transpose of matrix A
A_transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Print the transpose of matrix A
for row in A_transpose:
    print(row)
"""

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

txt = input("Enter a string: ")
x = re.compile("^a.*b$")
if x.search(txt):
    print("yes")
else:
    print("no")


