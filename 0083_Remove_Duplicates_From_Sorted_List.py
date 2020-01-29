from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist, to_list

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head: return None

    curr = interest = head

    while curr:
        if interest.value != curr.value:
            interest.next = curr
            interest = curr
        curr = curr.next

    interest.next = curr
    return head

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            to_list(deleteDuplicates(linkedlist([1, 1, 2]))),
            [1, 2]
        )

    def test_given_case_2(self):
        self.assertListEqual(
            to_list(deleteDuplicates(linkedlist([1, 1, 2, 3, 3]))),
            [1, 2, 3]
        )

    def test_empty_list(self):
        self.assertEqual(deleteDuplicates(None), None)

    def test_single_unique_node(self):
        node = ListNode(1)
        self.assertEqual(deleteDuplicates(node), node)

    def test_single_value_duplicated(self):
        self.assertListEqual(
            to_list(deleteDuplicates(linkedlist([1, 1]))),
            [1]
        )

    def test_multiple_values_unique(self):
        self.assertListEqual(
            to_list(deleteDuplicates(linkedlist([1, 2, 3, 4]))),
            [1, 2, 3, 4]
        )

    def test_multiple_values_duplicated(self):
        self.assertListEqual(
            to_list(deleteDuplicates(linkedlist([1, 1, 2, 2]))),
            [1, 2]
        )

if __name__ == "__main__":
    main()