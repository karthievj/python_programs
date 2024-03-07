def palindrome_string(s,n,i):
    if i>n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return palindrome_string(s,n,i+1)
    
s=input("Enter a word to check it is palindrome or not: ")
n=len(s)
a = palindrome_string(s,n,0)
if a:
    print("{} is a palindrome".format(s))
else:
    print("{} not a palindrome".format(s))