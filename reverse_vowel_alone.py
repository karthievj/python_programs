def reverseVowels(s):
    
    vowels = ["a","e","i","o","u","A","E","U","I","O"]
    
    vowel_track = []
    result = []
    count = 0
    for idx,val in enumerate(s):
        if val in vowels:
            result.append(count)
            vowel_track.append(val)
            count+=1
        else:
            result.append(val)

      
    final = {}
    print(vowel_track,"vowel_track")
    print(result,"result")
    reverse = vowel_track[::-1]
    print(reverse,"reverse")
    for idx,val in enumerate(reverse):
        final[idx]=val
    print(final,"final")
    
    for i in result:
        if i in final:
            position_to_insert = result.index(i)
            result.remove(i)
            result.insert(position_to_insert, final[i])
    print(result)
    
    return "".join(result)
a = reverseVowels(s ="race car")
print(a)