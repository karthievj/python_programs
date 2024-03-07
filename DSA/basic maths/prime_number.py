def prime_number(n):
    
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count ==2:
        return "is a prime number"
    else:
        return "is not a prime number"
    
n = int(input("enter a number to check whether it is prime or not: "))
result = prime_number(n)

print("{} {}".format(n,result))

def prime_numbers_in_specific_range(n):
    prime = []
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    
    
            
        
        


prime_numbers_in_specific_range(n)
