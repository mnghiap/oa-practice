def count_maximum_profitable_groups(stock_price):
    if len(stock_price) == 1:
        return 1
    if len(stock_price) == 2:
        return 2
    res = 3
    for i in range(2, len(stock_price)):
        res += 2
        max_is_left = stock_price[i-1] > stock_price[i]
        for j in range(i-2, -1, -1):
            if max_is_left:
                if stock_price[j] >= stock_price[j+1]:
                    res += 1
                else:
                    break
            else:
                res += 1
                max_is_left = stock_price[j] > stock_price[i]

    return res

print(count_maximum_profitable_groups([3, 1, 3, 5])) # 10
print(count_maximum_profitable_groups([1, 5, 2])) # 5
print(count_maximum_profitable_groups([2, 3, 2])) # 5
print(count_maximum_profitable_groups([1, 2, 3, 4, 5, 6, 7])) # 28
