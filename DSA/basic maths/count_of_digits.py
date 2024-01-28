def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

n=7785994
c = count_digits(n)
print("Number of digits present in {} is {}".format(n,c))



