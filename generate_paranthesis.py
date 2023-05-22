from itertools import product
n = 8
initiate = ""
paranthesises = "()"
result = []
for i in range(0,n):result+=paranthesises
s = ["(",")","{","}"]
print(list(product(s, repeat=4)))


    