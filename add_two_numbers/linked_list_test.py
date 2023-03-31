class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

L = LinkedList()

values = [1, 2, 3, 4, 5]

for value in values:
    L.add(value)

L.print()