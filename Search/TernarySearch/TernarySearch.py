# Time Complexity - O(log3 n)
# Space Complexity - O(1)

def ternary_search(array, search):
    low, high = 0, len(array)
    while high >= low:
        l_mid = low + (high-low)//3
        h_mid = high - (high-low)//3

        if array[l_mid] == search:
            return l_mid
        if array[h_mid] == search:
            return h_mid
        if search < array[l_mid]:
            high = l_mid-1
        elif search > array[h_mid]:
            low = h_mid + 1
        else:
            low = l_mid + 1
            high = h_mid - 1

    return None


def main():
    array = [1, 2, 5, 8, 13, 34, 56, 139, 150, 456]
    search = 139
    print(f'Searching element {search}')
    index = ternary_search(array, search)
    if index == None:
        print('Element not found')
    else:
        print(f'Element found at index {index}')


if __name__ == "__main__":
    main()
