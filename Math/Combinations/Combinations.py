def combination(arr: list, c_len: int):
    length = len(arr)
    comb_data = [None]*c_len
    combinationAfter(arr, length, c_len, 0, comb_data, 0)


def combinationAfter(arr: list, n: int, cn: int, aidx: int, data: list, didx: int):
    if (didx == cn):
        print(*data)
        return

    if (aidx >= n):
        return

    data[didx] = arr[aidx]
    aidx += 1

    combinationAfter(arr, n, cn, aidx, data, didx+1)
    combinationAfter(arr, n, cn, aidx, data, didx)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    c_len = 3
    combination(arr, c_len)
