
def make_dp_table(arr: list, dp: list):
    # Making the table is in O(n) time and space complexity
    dp[0] = 0
    for i in range(len(arr)):
        dp[i+1] = arr[i] + dp[i]

def range_sum(arr: list, query: list) -> list:
    dp = [None] * (len(arr)+1)
    make_dp_table(arr,dp)
    res = list()
    # Querying the result is in O(1) Time Complexity
    for low, up in query:
        res.append(dp[up+1]- dp[low])
    
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    query = [(1, 3), (2, 4)]
    print(*range_sum(arr, query))
