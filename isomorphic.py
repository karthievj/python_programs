def isomorphic(s,t):
    # import string
    
    hmap = dict()
    hmap1 = dict()
    for i in range(len(s)):
        hmap[s[i]] = i
        hmap1[t[i]] = i
    if list(hmap.values()) == list(hmap1.values()):
        return True
    return False  
    
a = isomorphic(s = "paper" , t = "title") 
print(a)
b = isomorphic(s = "foo" , t = "bar")
print(b)