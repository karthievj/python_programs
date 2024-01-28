
def pattern1(n):
    """
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * *
    """
    
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
        print()
    pass


def pattern2(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    
    for i in range(1,n+1):
        for j in range(0,i):
            print("*", end=" ")
        print()
    pass

def pattern3(n):
    """
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    
    for i in range(1,n+1):
        for j in range(1,i):
            print(j, end=" ")
        print()
    pass

def pattern4(n):
    """
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    
    for i in range(1,n+1):
        for j in range(0,i):
            print(i, end=" ")
        print()
    pass

def pattern5(n):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("*", end=" ")
        print()
    pass


def pattern6(n):
    """
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """
    
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j, end=" ")
        print()
    

def pattern7(n):
    
    """     
              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
    * * * * * * * * * * *
    """

    for i in range(0,n):
        for j in range(0,n-i+1):
            print(" ",end=" ")
        for j in range(0,i*2+1):
            print("*",end=" ")
        for j in range(0,n-i+1):
            print(" ",end=" ")
        print()
        
def pattern8(n):
    """
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
    """
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end=" ")
        for j in range(0,(2*n-(2*i+1))):
            print("*",end=" ")
        for j in range(0,i):
            print(" ",end=" ")
        print()
def pattern9(n):
    for i in range(0,2*n-1):
        stars = i
        if (i >n):
            stars = (2*n-i)
            for j in range(0,stars+1):
                print("*",end=" ")
            print()
            
            
def pattern10(n):
    """
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    """
    start =1
    for i in range(0,n):
        if (i%2==0):
            start = 1
        else:
            start = 0
        for j in range(0,i+1):
            print(start,end=" ")
            start = 1-start
        print()
        
def pattern11(n):
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    for i in range(0,n):
        for ch in range(65,(65+i)+1):
            print(chr(ch),end="")
        print()
    
        
def pattern12(n):
    """ 
    A
    B B
    C C C
    D D D D
    E E E E E
    F F F F F F
    """
    alph = 65
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(alph),end=" ")
        print()
        alph+=1
    

n = int(input("Enter how many rows you want to print: "))
pattern12(n)
