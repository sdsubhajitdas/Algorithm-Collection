from math import sqrt


def primeSieve(n: int) -> list:
    table = list(range(0, n+1))

    for i in range(2, int(sqrt(n))+1):
        if (table[i] == i):
            for j in range(i*i, n+1, i):
                if (table[j] == j):
                    table[j] = table[i]

    return table


def primeFactors(n: int, table: list) -> list:
    result = list()

    while (n != 1):
        result.append(table[n])
        n = n // table[n]

    return result


if __name__ == "__main__":
    n = [12246]
    table = primeSieve(max(n))
    for e in n:
        print(primeFactors(e, table))
