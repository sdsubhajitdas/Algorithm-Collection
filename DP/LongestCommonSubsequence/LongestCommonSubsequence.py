
def lcs_after(dp: list, a: str, b: str)->int:
    i, j = len(a), len(b)
    #print(f'A: {a}-{i}\tB: {b}-{j}')
    if (i == 0 or j == 0):
        dp[i][j] = 0
        return 0

    if (dp[i][j] != None):
        return dp[i][j]

    if (a[-1] == b[-1]):
        dp[i][j] = 1 + lcs_after(dp, a[:-1], b[:-1])
        return dp[i][j]
    else:
        dp[i][j] = max(lcs_after(dp, a[:-1], b), lcs_after(dp, a, b[:-1]))
        return dp[i][j]


def lcs(s1: str, s2: str) -> int:
    # O(M.N) for Space and Time Complexity

    dp = [[None]*(len(s1)+1) for _ in range(len(s2)+1)]
    return lcs_after(dp, s2, s1)


if __name__ == "__main__":
    s1 = 'aggtab'
    s2 = 'gxtxayb'
    print(lcs(s1, s2))
