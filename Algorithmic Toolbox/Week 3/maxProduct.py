n = int(input())
prices = sorted(list(map(int, input().split())))
clicks = sorted(list(map(int, input().split())))
value = [price*click for price, click in zip(prices, clicks)]
print(sum(value))