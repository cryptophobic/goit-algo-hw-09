def find_coins_greedy(coins, amount):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

def find_min_coins(coins, amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для нульової суми потрібна нульова кількість монет

    # Масив для зберігання останньої використаної монети
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin

    # Відновлюємо монети, які були використані для складання суми
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

coin_set = [50, 25, 10, 5, 2, 1]
amount = 113

# missing result: {50: 2, 10: 1, 2: 1, 1: 1}
print(f" find_coins_greedy() : {find_coins_greedy(coin_set, amount)}")
print(f" find_min_coins() :    {find_min_coins(coin_set, amount)}")