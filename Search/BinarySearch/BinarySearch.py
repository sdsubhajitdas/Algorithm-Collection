# Time Complexity - O(log n)
# Space Complexity - O(1)


def binary_search(array, search):
    low, high = 0, len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] > search:
            high = mid-1
        elif array[mid] < search:
            low = mid + 1
        else:
            return mid
    return None


def main():
    array = [1, 2, 5, 8, 13, 34, 56, 139, 150, 456]
    search = 5
    print(f'Searching element {search}')
    index = binary_search(array, search)
    if index == None:
        print('Element not found')
    else:
        print(f'Element found at index {index}')


if __name__ == "__main__":
    main()
