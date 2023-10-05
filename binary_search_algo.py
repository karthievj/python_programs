import random

#Populating a empty array with 200 values
array_len = 200
count = 1
arr = list()
while count <= array_len: 
    val = random.randint(0,500)
    if val not in arr:
        arr.append(val)
        count+=1
        
# sorting that array to execute the binary search
arr.sort()

print(arr)
# target value to find in the sorted array
target = random.choice(arr)
print(f'Target to find is {target}')

def binary_search(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        #efficient way to find the middle or middle = start+end//2
        middle = start + ((end-start) //2)
        if target == arr[middle]:
            return "{} is found in the array of index {}".format(target,middle)
        elif target > arr[middle]:
            start = middle+1
        else:
            end = middle-1  
    return f'{target} is not found in the array'  

print(binary_search(arr))

    