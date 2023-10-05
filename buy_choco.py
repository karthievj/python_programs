prices = [98,54,6,34,66,63,52,39]
money = 62
def se(prices,money):
    print(sorted(prices))
    print(sum(sorted(prices)[:2]))
    ans=money-sum(sorted(prices)[:2])
    if ans>=0:
        return ans
    return money 

print(se(prices,money))


    
    