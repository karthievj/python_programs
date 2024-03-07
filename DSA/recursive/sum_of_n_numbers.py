def sum_of_n_numbers(n):
    if n<1:
        return 0
    else:
        return n + sum_of_n_numbers(n-1)
    
if __name__=="__main__":
    n = int(input("Enter a number to find a sum of the n numbers: "))
    result = sum_of_n_numbers(n)
    print("The sum of first {} numbers is {}".format(n,result))