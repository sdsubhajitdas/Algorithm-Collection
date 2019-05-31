# Time Complexity - O(n)
# Space Complexity - O(1)

def linear_search(array,search):
    for idx,num in enumerate(array):
        if num == search:
            return idx
    return None


def main():
        array = [1, 2, 5, 8, 13, 34, 56, 139, 150, 456]
        search = 7
        print(f'Searching element {search}')
        index = linear_search(array, search)
        if index == None:
            print('Element not found')
        else:
            print(f'Element found at index {index}')


if __name__ == "__main__":
    main()
