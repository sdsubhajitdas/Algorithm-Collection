# Time Complexity - O(sqrt(n))
# Space Complexity - O(1)


import math


def jump_search(array, search):
    step = int(math.sqrt(len(array)))
    index = 0

    # Jumping Search
    while array[index] <= search:
        if array[index] == search:
            return index
        index += step

    last_index = index-step

    # Backward Linear Searching
    while index >= last_index:
        index -= 1
        if array[index] == search:
            return index

    return None


def main():
    array = [1, 2, 5, 8, 13, 34, 56, 139, 150, 456]
    search = 14
    print(f'Searching element {search}')
    index = jump_search(array, search)
    if index == None:
        print('Element not found')
    else:
        print(f'Element found at index {index}')


if __name__ == "__main__":
    main()
