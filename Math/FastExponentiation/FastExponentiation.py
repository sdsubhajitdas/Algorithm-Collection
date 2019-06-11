
def fast_exp(a: int, b: int) -> int:
    # O(log n) Complexity
    if (b == 1):
        return a
    if (b == 0):
        return 1

    r = fast_exp(a, b//2) % mod

    if (b % 2 == 0):
        return (r * r) % mod
    else:
        return (r * r * a) % mod


if __name__ == "__main__":
    global mod
    mod = 10**9 + 7
    print(fast_exp(2, 64))
