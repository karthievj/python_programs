nums = [-1]

l,r = 0, 0
length = len(nums)
result = []
while r < length:
	while r + 1 < length and nums[r+1] == nums[r]+1:
		r += 1
	
	if l == r:
		result.append(str(nums[l]))
	else:
		result.append(str(nums[l]) + "->" + str(nums[r]))
	r += 1
	l = r
print(result)