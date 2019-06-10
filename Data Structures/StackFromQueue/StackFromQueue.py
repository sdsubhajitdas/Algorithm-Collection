class StackFromQueue:
    def __init__(self, length: int):
        self.limit = length
        self.length = length
        self.que_1 = list()
        self.que_2 = list()

    def push(self, element: int):
        # O(n) Complexity
        if self.length == 0:
            print("Stack Overflow")
            return
        self.que_2.append(element)
        while len(self.que_1) != 0:
            self.que_2.append(self.que_1.pop(0))
        self.que_1, self.que_2 = self.que_2, self.que_1
        self.length -= 1

    def pop(self) -> int:
        # O(1) Complexity
        if self.length == self.limit:
            print("Stack Underflow")
            return
        self.length += 1 
        return self.que_1.pop(0)

    def peek(self) -> int:
        if self.length == self.limit:
            print("Stack Underflow")
            return
        return self.que_1[0]
    
    def __repr__(self):                     # To print the stack
        return str(self.que_1[::-1])


if __name__ == '__main__':
    sfq = StackFromQueue(3)
    sfq.pop()
    sfq.push(1)
    sfq.push(3)
    print(sfq)
    sfq.push(5)
    print(sfq)
    sfq.push(7)
    print(sfq)
    print(sfq.pop())
    print(sfq.pop())
    print(sfq.pop())
    
