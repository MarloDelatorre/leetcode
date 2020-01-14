from typing import Iterable, List

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

def to_list(node: ListNode) -> List:
    values = []
    while node is not None:
        values.append(node.value)
        node = node.next
    return values 

def linkedlist(values: Iterable) -> ListNode:
    sentinel = ListNode(None)
    tail = sentinel
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return sentinel.next