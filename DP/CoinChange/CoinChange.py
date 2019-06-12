def coin_change(coins: list, amt: int) -> int:
    # O(coins * amt) Time Complexity
    # O(amt) Space Complexity
    table = [amt+1]*(amt+1)
    table[0] = 0

    for i in range(1, amt+1):
        for coin in coins:
            if (i-coin < 0):
                break
            min_c = table[i-coin]
            table[i] = min(min_c+1, table[i])

    return table[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    res = coin_change(coins, amount)
    print(res if res-1 != amount else "None")
