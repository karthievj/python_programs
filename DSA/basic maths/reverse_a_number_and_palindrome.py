def reverse_number(n):
    dup = n
    msg = ""
    rev_num = 0
    
    while n > 0:
        last_digit = n % 10
        rev_num = (rev_num*10)+(last_digit)
        n = n//10
        
    if dup==rev_num:
        msg+= "{} is a palindrome".format(dup)
    else:
        msg+= "{} is not a palindrome".format(dup)

        
    return msg,rev_num
        
n = int(input("Enter a number to reverse: "))
msg,rev_num = reverse_number(n)
print("{} is the reverse of {}, {}".format(rev_num,n,msg))
