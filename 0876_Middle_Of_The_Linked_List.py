from datastructures.linkedlist import to_linkedlist, to_list, ListNode
from unittest import main, TestCase

def middleNode(head):
    if head is None:
        raise Exception("There must be at least one node in the linked list")
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow 

class Test(TestCase):
    def test_zero_nodes(self):
        with self.assertRaises(Exception):
            middleNode(None)
    
    def test_one_node(self):
        self.assertEqual(self.middle_node_value([1]), 1)

    def test_two_nodes(self):

        self.assertEqual(self.middle_node_value([1, 2]), 2)

    def test_odd_nodes(self):
        self.assertEqual(self.middle_node_value([1, 2, 3, 4, 5]), 3)

    def test_even_nodes(self):
        self.assertEqual(self.middle_node_value([1, 2, 3, 4, 5, 6, 7, 8]), 5)

    def middle_node_value(self, node):
        middle_node = middleNode(to_linkedlist(node))
        return middle_node.value

if __name__ == "__main__":
    main()