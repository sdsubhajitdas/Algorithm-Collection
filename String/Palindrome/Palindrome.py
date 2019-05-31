# Time Complexity - O(n)
# Space Complexity - O(1)

def main():
    word = input()
    start, end = 0, len(word)-1

    while (start < end):
        if word[start] != word[end]:
            print('Not Palindrome')
            return
        start += 1
        end -= 1
    print('Palindrome')


if __name__ == "__main__":
    main()
