
def fibonacciAfter(table: list, n: int) -> int:
    if n == 0 or n == 1:
        return table[n]

    if table[n] != None:
        return table[n]
    
    table[n] = fibonacciAfter(table, n-1) + fibonacciAfter(table, n- 2)

    return table[n]


def fibonacci(n: int) -> int:
    # O(n) Space Complexity
    table = [None]*n
    table[0], table[1] = 0, 1

    return fibonacciAfter(table, n-1)

if __name__ == "__main__":
    print(fibonacci(20))