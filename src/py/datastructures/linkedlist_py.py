class NodePy ():
    def __init__ (self, value, next):
        self.value = value
        self.next = next


class LinkedListPy ():
    def __init__ (self):
        self.head = NodePy(0, None)

    def push (self, value):
        new = NodePy(value, self.head)
        self.head = new

    def pop (self):
        self.head = self.head.next

    def __str__ (self):
        next = self.head
        s = ''
        while next:
            s += str(next.value) + ' '
            next = next.next
        return s
