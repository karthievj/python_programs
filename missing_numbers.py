def missing_numbers(nums):
    
    n = max(nums)
    
    expected_total = n*(n+1)//2
    print(expected_total)
    print(sum(nums))
    
nums = [0,1,3]
missing_numbers(nums)