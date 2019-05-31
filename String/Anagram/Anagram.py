# Time Complexity - O(n)
# Space Complexity - O(1)


def get_index(char):
    unicode = ord(char)
    if unicode >=65 and unicode <= 90:
        return unicode-65
    elif unicode >=97 and unicode <= 122:
        return unicode - 97 + 26
    elif unicode == 32:
        return 52
    else:
        raise Exception("Only A-Z and a-z are allowed")
    

def anagram(str1, str2):
    total_chars = 53
    frequency = [0]*total_chars

    if len(str1) != len(str2):
        print("Not Anagrams")

    for char1,char2 in zip(str1,str2):
        frequency[get_index(char1)] += 1
        frequency[get_index(char2)] -= 1

    if frequency.count(0) == total_chars: 
        print("Anagrams")
    else:
        print("Not Anagrams")





if __name__ == "__main__":
    str1 = input()
    str2 = input()
    anagram(str1,str2)