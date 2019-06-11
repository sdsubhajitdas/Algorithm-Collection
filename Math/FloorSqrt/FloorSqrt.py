def floor_sqrt(n: int) -> int:
    # O(n) Complexity (Binary Search Method)
    if (n == 0 or n == 1):
        return n

    start, end = 1, n
    ans = None

    while (start <= end):
        mid = (start + end)//2

        if (mid*mid == n):
            return mid

        if (mid*mid < n):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    
    return ans

if __name__ == "__main__":
    print(floor_sqrt(4))
    print(floor_sqrt(5))
    print(floor_sqrt(145))