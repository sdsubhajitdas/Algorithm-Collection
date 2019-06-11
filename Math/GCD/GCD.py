
def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)

    while (b!=0):
        a, b = b, a%b
    
    return a

if __name__ == "__main__":
    print(gcd(4,6))