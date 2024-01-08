def single_number(li):
    result = dict()
    
    for valu in li:
        result[valu] = li.count(valu)
        
    for i in result:
        if result[i]==1:
            return i
    

a = single_number(li=[3,2,3,3,34,5,5,5,6,6])
print(a)
