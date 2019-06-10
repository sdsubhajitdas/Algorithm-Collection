import math

# O(sqrt(n)) Complexity
def factors(n: int) -> list:
    result = list()
    index = 0
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            result.insert(index, i)
            if (i != n//i):
                result.insert(-(index + 1), n//i)
            index += 1
    return result


if __name__ == "__main__":
    print(*factors(16))
    print(*factors(15))
    print(*factors(17))
    print(*factors(105))
