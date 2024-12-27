def stockBuySell(A, n):
    minPrice = A[0]
    maxProfit = 0
    buySellPairs = []
    for i in range(1, n):
        if A[i] < minPrice:
            minPrice = A[i]
        else:
            profit = A[i] - minPrice
            if profit > maxProfit:
                maxProfit = profit
                buySellPairs.append((i-1, i))
    if not buySellPairs:
        return "No Profit"
    return buySellPairs

print(stockBuySell([822, 754, 1689, 305, 214 ,782 ,1463 ,1432 ,1382 ,1734 ,948 ,231 ,210 ,1676 ,877 ,670 ,1384, 725, 1370 ,412 ,724 ,371 ,928 ,358 ,533 ,1031 ,850 ,1555 ,1064 ,845 ,1692 ,514 ,630 ,1333 ,1640 ,315 ,1639 ,1792 ,1779 ,1325 ,1619 ,1400 ,378 ,145 ,913 ,901 ,1652 ,530 ,1259 ,880 ,303 ,685,1586], 53))
