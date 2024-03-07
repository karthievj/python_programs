def print_divisiors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
        # else:
        #     print("it is a prime number")
    print(divisors)
    return divisors
            

n = int(input("Enter a number to find its all divisors: "))
divisors = print_divisiors(n)
print("{} are the divisors of {}".format(divisors,n))
