def get_min_coins(money):
    coins = [1, 3, 4]
    min_num_coins = [0] + [float('inf')] * money

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]

money = int(input())
print(get_min_coins(money))
