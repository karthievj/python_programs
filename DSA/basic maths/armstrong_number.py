def armstrong_number(n):
    """_summary_

    Args:
        Armstromg number: if you do a digits of a number cube and add. the number itself will come this is called armstrong number
    """
    dup = n
    sum = 0
    msg = ""
    while n>0:
        last_digit = n%10    
        sum = sum + (last_digit*last_digit*last_digit)
        n=n//10
    if sum == dup:
        msg+= "{} is a armstrong number".format(dup)
    else:
        msg+= "{} is not a armstrong number".format(dup)
    
    return msg

n = int(input("Enter a number to check it is a armstrong or not: "))
result = armstrong_number(n)
print(result)