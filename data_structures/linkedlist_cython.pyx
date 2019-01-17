from libc.stdlib cimport malloc

cdef struct Node:
    int value
    Node* next

cdef class LinkedList:
    cdef Node* head
    cdef Node* new
    cdef void append (self, int val) nogil:
        if self.head == NULL:
            self.head = <Node*>malloc(sizeof(Node))
            self.head.value = val
            self.head.next = NULL
        else:
            new = <Node*>malloc(sizeof(Node))
            new.next = self.head
            new.value = val
            self.head = new

    cdef Node* current
    cdef void show (self):
        if self.head == NULL:
            print('empty')
        else:
            current = self.head
            while current != NULL:
                print(current.value)
                current = current.next


cpdef benchmark ():
    cdef int i
    cdef LinkedList L = LinkedList()
    for i in range(10000000):
        L.append(i)
