from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    curr_a, curr_b = headA, headB
    while curr_a or curr_b:
        if curr_a is curr_b:
            return curr_a
        curr_a = curr_a.next if curr_a else headB
        curr_b = curr_b.next if curr_b else headA

    return None

class Test(TestCase):
    def test_given_case_1(self):
        raise Exception("The current implementation of linkedlist does not support manipulating references")

if __name__ == "__main__":
    main()