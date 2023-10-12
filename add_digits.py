def addDigits(*args):
    for num in args: 
        while num >= 10:
                num = sum(int(i) for i in str(num))
    return num
        
if __name__== "__main__":
    a = 38
    print(addDigits(262124))