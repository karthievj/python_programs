from typing import List

def countFrequency(n: int, x: int, arr: List[int]) -> List[int]:
    count_dict = {}
    
    for i in range(1, x + 1):
        count_dict[i] = 0
    
    for num in arr:
        count_dict[num] += 1
    
    return [count_dict[i] for i in range(1, n + 1)]
    

# Example usage
n = 6
x = 9
arr = [1, 3, 1, 9, 2, 7]
result = countFrequency(n, x, arr)
print(result)
