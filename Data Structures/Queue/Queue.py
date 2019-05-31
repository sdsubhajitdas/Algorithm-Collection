class Queue():
    def __init__(self, length):
        self.length = length
        self.queue = [None]*length
        self.front, self.rear = -1, -1

    def enqueue(self, element):
        if self.front == self.length - 1:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.rear = 0

        self.front+=1
        self.queue[self.front] = element
        

    def dequeue(self):
        if self.rear == -1:
            print("Queue Underflow")
            return
        
        element = self.queue[self.rear]
        
        if self.rear == self.front:
            self.front, self.rear = -1, -1
        else:
            self.rear += 1
        
        return element
    
    def print(self):
        print(*self.queue[self.rear:self.front])


if __name__ == "__main__":
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.print()
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.print()