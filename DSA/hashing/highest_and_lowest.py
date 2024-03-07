def getFrequencies(v): 
    # Write your code here
    hashh = { }
    result = [ ]

    for i in range(1,len(v)+1):
        hashh[i] = 0

    for num in v:
        hashh[num] += 1
    print(hashh)

    a = list(hashh.values())
    print(max(a))

getFrequencies(v=[1,6, 2, 3, 1,4, 4,6])