details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
result = [ int(d[11:13]) for d in details if int(d[11:13])>=60]


print(result)
print(len(result))
