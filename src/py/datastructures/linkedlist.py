class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index):
        if not self.head:
            return None
        currNode = self.head
        for i in range(index):
            if not currNode.next:
                return None
            currNode = currNode.next
        return currNode.val
    
    def list(self):
        res = []
        currNode = self.head
        while currNode:
            res.append(currNode.val)
            currNode = currNode.next
        return res

    
    def insert(self, val, index):
        if not self.head and index == 0:
            self.head = Node(val)
        elif self.head and index == 0:
            self.head = Node(val, self.head)
        elif not self.head and index > 0:
            return None
        else:
            prevNode = self.head
            for i in range(index-1):
                if not prevNode.next:
                    return None
                prevNode = prevNode.next
            prevNode.next = Node(val, prevNode.next)
    
    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = Node(val)
    
    def pop(self, index=None):
        if index == None:
            if not self.head:
                return None
            if not self.head.next:
                res = self.head.val
                self.head = None
                return res
            prevNode = self.head
            currNode = prevNode.next
            while currNode.next:
                prevNode = currNode
                currNode = currNode.next
            res = currNode.val
            prevNode.next = None
            return res
        elif index == 0:
            if not self.head:
                return None
            if not self.head.next:
                res = self.head.val
                self.head = None
                return res
            res = self.head.val
            self.head = self.head.next
            return res
        else:
            if not self.head:
                return None
            if not self.head.next:
                return None
            prevNode = self.head
            currNode = prevNode.next
            for i in range(1, index):
                if not currNode.next:
                    return None
                prevNode = currNode
                currNode = currNode.next
            res = currNode.val
            prevNode.next = currNode.next
            return res
            