cnt=0
def recursion():
    global cnt
    if cnt>5:
        return
    else:
        print(cnt)
    cnt+=1
    recursion()
recursion()
