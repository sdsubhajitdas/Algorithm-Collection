def edit_distance(m: str, n: str) -> int:
    # O(m*n) Time and Space Complexity
    dp = [[None]*(len(n)+1) for _ in range(len(m)+1)]

    for i in range(len(m)+1):
        for j in range(len(n)+1):
            if (i == 0):
                dp[i][j] = j
            elif (j == 0):
                dp[i][j] = i
            elif (m[i-1] == n[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]
                )
    return dp[-1][-1]


if __name__ == "__main__":
    a = 'benyam'
    b = 'ephrem'
    print(edit_distance(a,b))
