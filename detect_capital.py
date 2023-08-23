def detctCapital(s):
    cap_letters = filter(str.isupper,s)
    capitals = ''.join(cap_letters)
    if len(capitals)==len(s):
        return True
    elif s.lower()==s:
        return True
    elif s[0]==s[0].upper() and len(capitals)<1:
        return True
    else:
        return False
    
    
q = detctCapital(s="SSa")
print(q)