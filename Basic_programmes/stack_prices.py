n=int(input("enter the no of stock prices:"))
prices=[]
for n in range(n):
    sp=int(input("enter the stock prices:"))
    prices.append(sp)
    highest_price=max(prices)
    lowest_price=min(prices)
profit=highest_price-lowest_price
print(profit)