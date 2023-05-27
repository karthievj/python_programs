import re
def subSequence(s,t):
    v = list(s)
    print(v)
    r = ".*".join(v)
    print(r)
    a = re.search("".join(list(s)),t)
    print(a)
    
    
  
a= subSequence(s="ab",t="baab")
print(a)
