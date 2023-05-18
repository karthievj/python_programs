def happy_num(n):
    # val = n
    result = []
    set_ = set()
    while n!=1:
        for i in str(n):
            # while val>1:
            i = int(i)
            a = i*i
            result.append(a)
        n = sum(result)
        if n in set_:
            return False
        else:
            set_.add(n)
            result.clear()
    return True
        
a = happy_num(n=19)
print(a)

    