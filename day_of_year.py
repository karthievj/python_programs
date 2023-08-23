from datetime import datetime
def dayofyear(date):
    list_year=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    day=int(date[-2:])
    year=int(date[:4])
    month=int(date[5:7])

    # if year is leap and february is gone, add an extra day 
    if year%4==0 and year!=1900 and month>2 :
        day+=1

    #return days of specific month + date
    return list_year[month-1]+day

    
a = dayofyear(date='2024-03-14')
print(a)