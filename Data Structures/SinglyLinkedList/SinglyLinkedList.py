class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList():
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
            return self.start.next.value if self.length > 0 else None

        elif index == -1 or index >= self.length:
            node_i = self.start
            while node_i.next != None:
                node_i = node_i.next
            return node_i.value
        else:
            i = 0
            node_i = self.start
            while i <= index:
                node_i = node_i.next
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
        node_2 = self.start.next  # (i)th node
        i = 0
        while i < index:
            i += 1
            node_1 = node_2
            node_2 = node_2.next

        node_1.next = node_2.next
        self.length -= 1

    def _add_at_beginning(self, element):
        node_2 = self.start.next     # Will become the 2nd node
        node_1 = Node(value=element, next=node_2)
        self.start.next = node_1
        self.length += 1

    def _add_at_end(self, element):
        node_i = self.start
        while node_i.next != None:
            node_i = node_i.next
        node_i.next = Node(element)
        self.length += 1

    def _add_at_index(self, element, index):
        if self.length == 0:
            self._add_at_beginning(element)
            return
        elif index >= self.length:
            self._add_at_end(element)
            return

        node_1 = self.start  # (i-1)th node
        node_2 = self.start.next  # (i)th node
        i = 0
        while i < index:
            node_1 = node_2
            node_2 = node_2.next
            i += 1
        node = Node(element, node_2)
        node_1.next = node
        self.length += 1

    def print(self):
        node_i = self.start.next
        while node_i != None:
            print(node_i.value, end=' ')
            node_i = node_i.next
        print()


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.add(3, 10)
    sll.add(1, 0)
    sll.add(5, 0)
    sll.add(9, -1)
    sll.add(2, -1)
    sll.add(10, -1)
    sll.add(4, 0)
    sll.print()
    print(sll.get(0))
    print(sll.get(-1))
    print(sll.get(10))
    print(sll.get(5))
    sll.delete(3)
    sll.print()
