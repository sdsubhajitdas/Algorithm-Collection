class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def _index(self, c):
        return ord(c)-ord('a')

    def insert(self, word: str):
        word = word.lower()
        troot = self.root
        for ch in word:
            idx = self._index(ch)
            if (troot.child[idx] == None):
                troot.child[idx] = Node()
            troot = troot.child[idx]
        troot.end = True

    def search(self, key: str):
        troot = self.root
        for ch in key:
            idx = self._index(ch)
            if(troot.child[idx] == None):
                return False
            troot = troot.child[idx]
        return True

    def __repr__(self):
        res = list()
        self._print(res, self.root, "")
        return '\n'.join(res)

    def _print(self, res: list, node: Node, word: str):
        if (node == None):
            return
        if (node.end == True):
            res.append(word)

        for idx in range(26):
            if (node.child[idx] != None):
                c = chr(ord('a') + idx)
                self._print(res, node.child[idx], word + c)

    def print_tree(self, node: Node = None, space=0):
        if (space == 0):
            print('root:')
        if (node == None):
            node = self.root
        for idx, child in enumerate(node.child):
            if (child != None):
                print(f'{" "*space}|{"-"}{chr(ord("a") + idx)}')
                self.print_tree(child, space+2)


if __name__ == "__main__":
    trie = Trie()
    trie.insert('abcd')
    trie.insert('subhajit')
    trie.insert('geeksforgeeks')
    trie.insert('graphics')
    print(trie)
    print(trie.search('sub'))
    print(trie.search('acid'))
    print(trie.search('gee'))
    # trie.print_tree()
