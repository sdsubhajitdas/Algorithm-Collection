# Space Complexity - O(n)
# Time Complexity
    # get_sum - O(log n)
    # update  - O(log n)

class FenwickTree:
    def __init__(self, l: int, arr: list = None):
        self.l = l
        self.tree = [0]*(l+1)

        if arr:
            self._construct(arr)

    def get_sum(self, idx: int) -> int:
        s = 0
        idx += 1
        while(idx > 0):
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def update(self, idx: int, val: int):
        idx += 1

        while(idx <= self.l):
            self.tree[idx] += val
            idx += idx & (-idx)

    def _construct(self, arr: list):
        for idx, ai in enumerate(arr):
            self.update(idx, ai)

    def __repr__(self):
        return str(self.tree)



if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    bit = FenwickTree(n,arr)
    bit.update(2,2)
    print(bit.get_sum(3))