nums = [-2, -1]
print(nums)
result = []
if len(nums)==0:
    print("[]")
elif len(nums)==1:
    result.append(str(nums[0]))
else:
    if nums[0]>=0:
        li_ = [i for i in range(0,nums[-1]+1)]
        print(li_)
        track = []
        result = []

        # function to format the output
        def result_():
            if len(track)>1:
                range_ = '{}->{}'.format(track[0], track[-1])
                result.append(range_)
                track.clear()
                
        for val in li_:
            if val in nums:
                track.append(val)
            elif len(track)==1:
                result.append(str(track[0]))
                track.clear()
            else:
                result_()

        # Checking whether the track list is having a single element
        if len(track)==1:
            result.append(str(track[0]))
        else:
            result_()
            



