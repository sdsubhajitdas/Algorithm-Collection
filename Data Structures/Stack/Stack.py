class Stack():
    def __init__(self,length):
        self.length = length
        self.stack = [None]*length
        self.pointer = -1
    
    def push(self, element):
        if self.pointer >=self.length-1:
            print("Stack Overflow")
            return
        self.pointer+=1
        self.stack[self.pointer]=element
    
    def pop(self):
        if self.pointer < 0:
            print("Stack Underflow")
            return
        self.pointer-=1
        return self.stack[self.pointer + 1]

    def peek(self):
        return self.stack[self.pointer] if self.pointer >= 0 else None
    
    def print(self):
        print(*self.stack if self.pointer>=0 else None)


if __name__ == "__main__":
    stack = Stack(3)
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(8)
    print(stack.peek())
    stack.print()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())