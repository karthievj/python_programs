arr = ["one.two.three","four.five","six"]
arr1 = ["$easy$","$problem$"]
separator = "."
result = []
for i in arr:
    if separator in i:
        a = i.split(separator)
        print(a)
        for j in a:
            if len(j)!=0:
                result.append(j)
    else:
        result.append(i)
print(result)
        