while True:
    num = int(input("Enter a number to check whether it is prime or not: "))
    def prime_number(num):
        for k in range(2,num):
            if num %k == 0:
                result = "{} is not a prime number".format(num)
                return result
        return "{} is a prime number".format(num)
    print(prime_number(num))
            
    