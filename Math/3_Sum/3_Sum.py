def sum3_n2(array: list, s: int) -> tuple:
    length = len(array)
    array = sorted(array)

    for i in range(length-2):
        l = i+1
        r = length - 1
        while(l < r):
            if (array[i]+array[l]+array[r] == s):
                return array[i], array[l], array[r]
            elif (array[i]+array[l]+array[r] < s):
                l += 1
            else:
                r -= 1
    return None


def sum3_n(array: list, s: int) -> tuple:
    length = len(array)

    for i in range(length):
        table = dict()
        cur_s = s - array[i]
        for j in range(i+1, length):
            if(table.get(cur_s - array[j], -1) == True):
                return array[i], cur_s - array[j], array[j]
            table[array[j]] = True
    return None


if __name__ == "__main__":
    array = [1, 4, 45, 6, 10, 8]
    s = 22

    # sum3_n2() function is an O(n^2) approach towards the problem
    print(sum3_n2(array, s))

    # sum_n() function uses a hashing table
    print(sum3_n(array, s))
