
def lcm(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    ab = a*b
    while (b != 0):
        a, b = b, a % b

    return ab // a

if __name__ == "__main__":
    print(lcm(7,5))