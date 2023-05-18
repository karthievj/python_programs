def valid(s):
    stack = []

    rule = {
        ")":"(",
        "}":"{",
        "]":"[",  
    }
    result = None
    for i in s:
        if len(s)>1:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
                
            elif i==")" or i=="}" or i=="]":
                if len(stack)>0:
                    if rule[i]==stack[-1]:
                        stack.pop()
                    else:
                        return False  
                else:
                    return False
        else:
            return False
        
    if len(stack)==0:
        return True
    else:
        return False   
            
result = valid(s ="([])))")
        
print(result)

        
        
    