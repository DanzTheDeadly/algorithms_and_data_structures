from libc.stdlib cimport malloc, free

cdef struct Node:
    int value
    Node* next


cdef class Queue:
    cdef:
        Node* head
        Node* tail
        int size

    def __cinit__ (self):
        self.head = NULL
        self.tail = NULL
        self.size = 0


    def __str__ (self):
        cdef:
            str res = ''
            Node* curr = self.head
        while curr != NULL:
            res += str(curr.value) + ' '
            curr = curr.next
        return res


    cpdef void enqueue (self, value):
        cdef:
            Node* new = <Node*>malloc(sizeof(Node))
            Node* curr = self.head
        new.value = value
        new.next = NULL
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1


    cpdef dequeue (self):
        cdef:
            int ret = self.head.value
            Node* dealloc = self.head
        if self.size == 0:
            return None
        else:
            self.head = self.head.next
            free(dealloc)
            self.size -= 1
            return ret
