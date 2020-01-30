from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist, to_list

def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next: return head 

    curr_odd = head
    curr_even = head.next
    head_even = curr_even

    while curr_even and curr_even.next:
        curr_odd.next = curr_even.next
        curr_even.next = curr_odd.next.next
        curr_odd = curr_odd.next
        curr_even = curr_even.next

    curr_odd.next = head_even
    return head

class Test(TestCase):
    def test_empty_list(self):
        self.assertEqual(oddEvenList(None), None)

    def test_single_node(self):
        self.assertListEqual(to_list(oddEvenList(ListNode(1))), [1])

    def test_two_nodes(self):
        self.assertListEqual(to_list(oddEvenList(linkedlist([1, 2]))), [1, 2])

    def test_multiple_odd(self):
        self.assertListEqual(
            to_list(oddEvenList(linkedlist([1, 2, 3, 4, 5]))),
            [1, 3, 5, 2, 4]
        )

    def test_multiple_even(self):
        self.assertListEqual(
            to_list(oddEvenList(linkedlist([1, 2, 3, 4, 5, 6]))),
            [1, 3, 5, 2, 4, 6]
        )

if __name__ == "__main__":
    main()