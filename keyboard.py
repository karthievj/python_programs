def key(words):
    key_list1 = "qwertyuiop"
    key_list2 = "asdfghjkl"
    key_list3 = "zxcvbnm"
    final_list = []
    
    for i in range(0, len(words)):
        each_word = words[i]
        key_list = validate(each_word,key_list1,key_list2,key_list3)
        for count,letter in enumerate(each_word.lower()):
            if letter in list(key_list):
                if len(each_word)==count+1:
                    final_list.append(each_word)
                else:
                    continue
            else:
                break
            
    return final_list
        
def validate(s,key_list1,key_list2,key_list3):
    for i in s:
        if i.lower() in key_list1:
            return key_list1
        elif i.lower() in key_list2:
            return key_list2
        elif i.lower() in key_list3:
            return key_list3

a = key(words=["zxcvbne","Alaska","Dad","Peace"])
print(a)