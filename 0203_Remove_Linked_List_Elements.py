from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist, to_list 

def removeElements(head: ListNode, val: int) -> ListNode:
    if not head:
        return None

    prev, curr = None, head
    while curr:
        next = curr.next
        if curr.value == val:
            if curr == head:
                head = next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return head

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            to_list(removeElements(linkedlist([1, 2, 6, 3, 4, 5]), 6)),
            [1, 2, 3, 4, 5]
        )

    def test_list_is_none(self):
        self.assertIsNone(removeElements(None, 1))

    def test_remove_only_value(self):
        self.assertIsNone(removeElements(linkedlist([1]), 1))

    def test_remove_head(self):
        self.assertListEqual(
            to_list(removeElements(linkedlist([2, 1]), 2)),
            [1]
        )

    def test_remove_tail(self):
        self.assertListEqual(
            to_list(removeElements(linkedlist([1, 2]), 2)),
            [1]
        )

    def test_remove_middle_node(self):
        self.assertListEqual(
            to_list(removeElements(linkedlist([1, 2, 3]), 2)),
            [1, 3]
        )

    def test_remove_all_are_removed_value(self):
        self.assertIsNone(removeElements(linkedlist([2, 2, 2]), 2))

if __name__ == "__main__":
    main()