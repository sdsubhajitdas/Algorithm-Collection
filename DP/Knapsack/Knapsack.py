
def knapsack(weights: list, values: list, lw: int) -> int:
    # O(items*lw) Time and Space Complexity
    dp = [[0]*(lw+1) for _ in values]
    items = len(weights)

    for i in range(items):
        for w in range(lw+1):
            if (w < weights[i]):
                dp[i][w] = 0
            else:
                taken = dp[i-1][w-weights[i]] + values[i]
                not_taken = dp[i-1][w]
                dp[i][w] = max(taken, not_taken)
    return dp[-1][-1]


if __name__ == "__main__":
    values = [6, 10, 12]
    weights = [1, 2, 3]
    limit_w = 5

    print(knapsack(weights, values, limit_w))
