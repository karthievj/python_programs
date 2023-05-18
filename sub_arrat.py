strs = ["cir","car","cap"]
if len(strs) == 0:
    print("")
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if (i == len(word) or word[i] != base[i]):
                print(base[0:i])
# print(strs[1:])


    

        