s = "{[]}"
brackets = {"{":"}","[":"]","(":")"}
count = 0
for i in s:
    i=str(i)
    a = s[count+1]
    if len(s)>1:
        if i=="{" or i=="(" or i=="[":
            b = brackets[i]
            if i==a:
                count=0
                print("false")
                continue
            else:
                if a==b:
                    
                    print("True")
                    count+=1
                else:
                    print("false")
                    count+=1
            
    else:
        print("false")
        