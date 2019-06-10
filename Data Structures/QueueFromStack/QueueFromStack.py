class QueueFromStack:
    def __init__(self, length: int):
        self.length = length
        self.limit = length
        self.stack1 = list()
        self.stack2 = list()

    def enqueue(self, element: int):
        # O(n) Complexity
        if self.length <= 0:
            print("Queue Full")
            return

        while (len(self.stack1) != 0):
            self.stack2.append(self.stack1.pop())

        self.stack1.append(element)

        while (len(self.stack2) != 0):
            self.stack1.append(self.stack2.pop())

        self.length -= 1

    def dequeue(self) -> int:
        # O(1) Complexity
        if (self.length == self.limit):
            print("Queue Empty")
            return
        self.length += 1
        return self.stack1.pop()

    def print(self):
        print(*self.stack1[::-1])


if __name__ == "__main__":
    queue = QueueFromStack(4)
    queue.dequeue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.print()
    queue.enqueue(8)
    queue.print()
    queue.enqueue(10)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
