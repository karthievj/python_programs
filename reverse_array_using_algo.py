def reverse_array(arr):
    first = 0
    last = len(arr) - 1
    
    """Need to create one while loop to iterate over this"""
    
    while first < last :
        # make a swap of the element
        arr[first], arr[last] = arr[last] , arr[first]
        first += 1
        last -= 1
    
    return arr


if __name__== "__main__":
    arr1 = [3,5,8,1,55,890]
    arr2 = list('Hello')
    arr3 = []
    arr4 = [0]
    
print(reverse_array(arr1))