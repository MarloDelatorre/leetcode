from unittest import TestCase, main

from datastructures.linkedlist import ListNode, linkedlist 

def isPalindrome(head: ListNode) -> bool:
    back_head = head

    def is_palindrome(head: ListNode) -> bool:
        if not head:
            return True

        is_pal = is_palindrome(head.next)
        nonlocal back_head
        is_eq = head.value == back_head.value
        back_head = back_head.next
        return is_pal and is_eq

    return is_palindrome(head)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertFalse(isPalindrome(linkedlist([1, 2])))

    def test_given_case_2(self):
        self.assertTrue(isPalindrome(linkedlist([1, 2, 2, 1])))
        
    def test_empty_list(self):
        self.assertTrue(isPalindrome(None))

    def test_single_node(self):
        self.assertTrue(isPalindrome(ListNode(1)))

    def test_odd_length_palindrome(self):
        self.assertTrue(isPalindrome(linkedlist([1, 2, 3, 2, 1])))

    def test_odd_length_not_palindrome(self):
        self.assertFalse(isPalindrome(linkedlist([1, 2, 3, 4, 1])))
    
if __name__ == "__main__":
    main()