class Node():
    def __init__(self, value=None, before=None, after=None):
        self.value = value
        self.before = before
        self.after = after


class DoublyLinkedList():
    def __init__(self):
        # Initial pointer contains no value.
        self.start = Node()
        self.length = 0

    def add(self, element, index):
        '''
        index = 0  -- beginning of list
        index = -1 -- end of list
        index = x  -- index if inside length or at the end.
        '''
        if index == 0:
            self._add_at_beginning(element)
        elif index == -1:
            self._add_at_end(element)
        else:
            self._add_at_index(element, index)
            pass

    def get(self, index):
        '''
        index = 0  -- beginning of list
        index = -1 -- end of list
        index = x  -- index if inside length or at the end.
        '''
        if index == 0 or self.length == 1:
            return self.start.after.value if self.length > 0 else None

        elif index == -1 or index >= self.length:
            node_i = self.start
            while node_i.after != None:
                node_i = node_i.after
            return node_i.value
        else:
            i = 0
            node_i = self.start
            while i <= index:
                node_i = node_i.after
                i += 1
            return node_i.value

    def delete(self, index):
        '''
        Index should be inside range
        -1 index means last element
        '''
        if index == -1:
            index = self.length - 1
        if index >= self.length:
            print('Deletion cant be done Index Out Of Bounds')
            return

        node_1 = self.start  # (i-1)th node
        node_2 = self.start.after  # (i)th node
        i = 0
        while i < index:
            i += 1
            node_1 = node_2
            node_2 = node_2.after
        
        node_3 = node_2.after
        node_1.after = node_3
        if node_3!= None:
            node_3.before = node_1
        self.length -=1

    def _add_at_beginning(self, element):
        node_2 = self.start.after     # Will become the 2nd node
        node_1 = Node(value=element, before=self.start, after=node_2)
        self.start.after = node_1
        if node_2 != None:
            node_2.before = node_1
        self.length += 1

    def _add_at_end(self, element):
        node_i = self.start
        while node_i.after != None:
            node_i = node_i.after
        node_i.after = Node(element,before=node_i)
        self.length += 1

    def _add_at_index(self, element, index):
        if self.length == 0:
            self._add_at_beginning(element)
            return
        elif index >= self.length:
            self._add_at_end(element)
            return

        node_1 = self.start  # (i-1)th node
        node_2 = self.start.after  # (i)th node
        i = 0
        while i < index:
            node_1 = node_2
            node_2 = node_2.after
            i += 1
        node = Node(element,node_1, node_2)
        node_2.before = node
        node_1.after = node
        self.length +=1

    def print(self):
        node_i = self.start.after
        while node_i != None:
            print(node_i.value, end=' ')
            node_i = node_i.after
        print()
    
    def print_reverse(self):
        node_i = self.start.after
        while node_i.after != None:
            node_i = node_i.after
        
        while node_i != self.start:
            print(node_i.value, end=' ')
            node_i = node_i.before
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add(1,0)
    dll.add(2,0)
    dll.add(3,-1)
    dll.add(4,-1)
    dll.add(0,1)
    dll.add(5,3)
    dll.print()
    dll.print_reverse()
    print(dll.get(0))
    print(dll.get(-1))
    print(dll.get(3))
    dll.delete(0)
    dll.delete(1)
    dll.delete(-1)
    dll.print()
    dll.print_reverse()
