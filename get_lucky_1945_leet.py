def getLucky(s, k) -> int:
    val = []    
    for i in s:
        initial = 96
        val.append(ord(i)- initial)  
         
    result = ""
    for j in val:
        result+= str(j) 
    count = 1
    while count <=k:
        ans = 0
        for r in result:
            ans+= int(r)
        result = str(ans)
        count+= 1
    print(ans)

    

getLucky("leetcode",2)