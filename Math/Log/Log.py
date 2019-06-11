
def log(n: float, base: int) -> float:
    #O(log n) Complexity
    return (1 + log(n//base, base)) if (n > base - 1) else 0


if __name__ == "__main__":
    print(log(1024, 3))
