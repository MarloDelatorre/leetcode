from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist, to_list

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry, sentinel = 0, ListNode(None)
    head = sentinel

    while l1 or l2:
        sum = carry 
        if l1:
            sum += l1.value
            l1 = l1.next
        if l2:
            sum += l2.value
            l2 = l2.next
        head.next = ListNode(sum % 10) 
        carry = sum // 10 
        head = head.next

    if carry:
        head.next = ListNode(1)

    return sentinel.next

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            to_list(addTwoNumbers(linkedlist([2, 4, 3]), linkedlist([5, 6, 4]))),
            [7, 0, 8]
        )

    def test_carry_single_digits(self):
        self.assertListEqual(
            to_list(addTwoNumbers(ListNode(1), ListNode(9))),
            [0, 1]
        )

    def test_diff_lengths_and_bubble_carry(self):
        self.assertListEqual(
            to_list(addTwoNumbers(linkedlist([9, 9, 9]), ListNode(1))),
            [0, 0, 0, 1]
        )

if __name__ == "__main__":
    main()