from ..datastructures.linkedlist_py import Node

def merge(l1, l2):
    '''
    Merge 2 sorted linked lists into one
    '''
    if not l1:
        return l2
    if not l2:
        return l1
    head = tail = Node()
    # step 3
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # step 4
    tail.next = l1 or l2
    # step 5
    return head.next