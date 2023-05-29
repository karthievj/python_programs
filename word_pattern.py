def word_pattern(pattern,s):
    splitted= s.split()
    track = {}
    if len(pattern)==len(splitted):
        for i in range(0,len(pattern)):
            if pattern[i] not in track :
                d = track.values()
                if splitted[i] not in track.values():
                    track[pattern[i]]=splitted[i]
                else:
                    return False
            else:
                if track[pattern[i]]==splitted[i] :
                    pass
                else:
                    return False
            
        return True
    else:
        return False

a = word_pattern(pattern = "aaa", s = "aa aa aa aa")
b = word_pattern(pattern = "abba", s = "dog cat cat dog")
print(a)
print(b)