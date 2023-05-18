# to finf the first repeating number in python


a = [1, 4, 7, 7, 6, 4, 6,6]
k = 3
n = len(a)
hashmap = {}

for i in range(0, n):
    
    if a[i] in hashmap:
        hashmap[a[i]]+=1
        
    else:
        hashmap[a[i]]=1
        
    if(hashmap[a[i]]==k):
            print(a[i])
print(hashmap)


            