'''
A nice explanation of this method can be found here
https://www.geeksforgeeks.org/fibonacci-search/
'''

# Time Complexity - O(log n)
# Space Complexity - O(1)

def fibonacci_search(array, search):

    # (n-2)th, (n-1)th, n-th Fibonacci number
    fib_2, fib_1, fib = 0, 1, 1
    length = len(array)
    offset = 0

    while fib < length:
        fib_2 = fib_1
        fib_1 = fib
        fib = fib_1 + fib_2
    
    while fib > 1:
        index = min(offset + fib_2,length-1)

        if array[index] < search:
            fib = fib_1
            fib_1 = fib_2
            fib_2 = fib - fib_1
            offset = index
        elif array[index] > search:
            fib = fib_2
            fib_1 -= fib_2
            fib_2 = fib - fib_1
        else:
            return index
    
    return None
    



def main():
    array = [1, 2, 5, 8, 13, 34, 56, 139, 150, 456, 490]
    search = 500
    print(f'Searching element {search}')
    index = fibonacci_search(array, search)
    if index == None:
        print('Element not found')
    else:
        print(f'Element found at index {index}')


if __name__ == "__main__":
    main()
