def maxProfit(prices):
    min_price = min(prices)
    if prices.index(min_price) != (len(prices) - 1):
        after_buyList = prices[prices.index(min_price):]
        max_priceAfterbuy = max(after_buyList)
        return max_priceAfterbuy - min_price
        
    else:
        return 0
a = maxProfit(prices= [1,2]) 
print(a)