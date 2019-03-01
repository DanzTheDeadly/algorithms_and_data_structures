from libc.stdlib cimport malloc

cdef struct Node:
    int value
    Node* next

cdef class LinkedList:
    cdef Node* head
    cdef void append (self, int val) nogil:
        cdef Node* new
        if self.head == NULL:
            self.head = <Node*>malloc(sizeof(Node))
            self.head.value = val
            self.head.next = NULL
        else:
            new = <Node*>malloc(sizeof(Node))
            new.next = self.head
            new.value = val
            self.head = new


    cdef void show (self):
        cdef Node* current
        if self.head == NULL:
            print('empty')
        else:
            current = self.head
            while current != NULL:
                print(current.value)
                current = current.next
