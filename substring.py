def sub_string(s):
    str_1, str_2 = '', ''
    for i in range(len(s)):
        if s[i] in str_1:
            if len(str_1) > len(str_2): 
                str_2 = str_1
            str_1 = str_1[str_1.index(s[i])+1:] + s[i]
        else: 
            str_1 += s[i]
    return max(len(str_1), len(str_2))

a = sub_string(s = "dvdf")
b = sub_string(s="abceabbb")
print(a)  
print(b)   
    
    