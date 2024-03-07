def factorial_of_n_numbers(n):
    if n==0:
        return 1
    else:
        return n * factorial_of_n_numbers(n-1)
    
if __name__=="__main__":
    n = int(input("Enter a number to find its factorial: "))
    result = factorial_of_n_numbers(n)
    print("The fcatorial of  {} is {}".format(n,result))