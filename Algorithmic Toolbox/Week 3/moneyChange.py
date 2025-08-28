money = int(input())
coin_10 = money // 10
money = money % 10
coin_5 = money // 5
money = money % 5
coin_1 = money // 1
print(coin_1 + coin_5 + coin_10)