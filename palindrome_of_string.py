import re 
s ="a man, a plan, a canal: Panama"
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9]+',"", s)
print(s)