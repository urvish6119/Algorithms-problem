stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
minimum = min(stock_prices_yesterday)
print(minimum)
print(stock_prices_yesterday.index(5))
for x in stock_prices_yesterday[2:]:
    maximum = max(stock_prices_yesterday)

print(maximum)
profit = maximum - minimum;
print(profit)
print('you can made $ profit ')