"""
Test Cases for better understanding

Example 1
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Example 3:
Input: s = "race car"
Output: "race car"
"""

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
    reverse = vowel_track[::-1]
    for idx,val in enumerate(reverse):
        final[idx]=val
    
    for i in result:
        if i in final:
            position_to_insert = result.index(i)
            result.remove(i)
            result.insert(position_to_insert, final[i])
    
    return "".join(result)

a = reverseVowels(s ="race car")
print(a)