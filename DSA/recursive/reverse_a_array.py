def reverse_array(i,arr,n):
    if i>=n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    reverse_array(i+1,arr,n)
    
i=0
arr=[1,2,3,4,5]
n=len(arr)
reverse_array(i,arr,n)

print("Original array: {}, reversed array:{}".format(arr,arr))