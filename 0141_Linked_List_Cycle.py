from unittest import TestCase, main

from datastructures.linkedlist import ListNode

def hasCycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = fast = head
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

class Test(TestCase):
    def test_given_case(self):
        raise NotImplementedError("linkedlist implementation doesn't support circlular lists")

if __name__ == "__main__":
    main()