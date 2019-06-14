
def max_sum_subarray(arr: list) -> int:
    # O(N) time and space complexity
    dp = [None] * len(arr)
    dp[0] = arr[0]

    for idx in range(1, len(arr)):
        sum_sofar = dp[idx-1] + arr[idx]
        dp[idx] = sum_sofar if (sum_sofar > arr[idx]) else arr[idx]

    return max(dp)


if __name__ == "__main__":
    #arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    #arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sum_subarray(arr))
