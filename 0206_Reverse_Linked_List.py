from unittest import main, TestCase
from datastructures.linkedlist import ListNode, to_linkedlist, to_list

def reverseList(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev 
        prev = head
        head = next
    return prev 

class Test(TestCase):
    def test_given_case(self):
        values = [1, 2, 3, 4, 5]
        rev_list = reverseList(to_linkedlist(values))
        self.assertListEqual(
            to_list(rev_list),
            values[::-1]
        )

    def test_empty_list(self):
        values = []
        rev_list = reverseList(to_linkedlist(values))
        self.assertListEqual(
            to_list(rev_list),
            []
        )
    
    def test_single_value(self):
        values = [1]
        rev_list = reverseList(to_linkedlist(values))
        self.assertListEqual(
            to_list(rev_list),
            [1]
        )

if __name__ == "__main__":
    main()