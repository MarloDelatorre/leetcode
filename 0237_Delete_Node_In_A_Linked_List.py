from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist, to_list

def deleteNode(node: ListNode) -> None:
    node.value, node.next = node.next.value, node.next.next

class Test(TestCase):
    def test_base_case(self):
        head = ListNode(4)
        head.next = ListNode(2)
        deleteNode(head)
        self.assertListEqual(to_list(head), [2])

    def test_multiple_remove_head(self):
        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        deleteNode(head)
        self.assertListEqual(to_list(head), [2, 3])

    def test_multiple_remove_middle(self):
        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        deleteNode(head.next)
        self.assertListEqual(to_list(head), [4, 3])

if __name__ == "__main__":
    main()