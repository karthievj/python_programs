def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

n = int(input("Enter a number to check how many digits it had: "))
c = count_digits(n)
print("{} is a {} digit number ".format(n,c))



