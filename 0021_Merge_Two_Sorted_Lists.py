import unittest
from datastructures.linkedlist import ListNode, linkedlist, to_list

class Solution():
    @staticmethod
    def merge(list1, list2):
        sentinel = ListNode(None)
        tail = sentinel
        while list1 is not None and list2 is not None:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1 is None:
            tail.next = list2
        if list2 is None:
            tail.next = list1

        return sentinel.next

class Test(unittest.TestCase):
    def test_given_case(self):
        merged = Solution.merge(
            linkedlist([1,2,4]),
            linkedlist([1,3,4])
        )
        self.assertListEqual(
            to_list(merged),
            [1,1,2,3,4,4]
        )

    def test_empty_case(self):
        merged = Solution.merge(
            linkedlist([]),
            linkedlist([])
        )
        self.assertListEqual(
            to_list(merged),
            []
        )

    def test_first_empty_second_not(self):
        merged = Solution.merge(
            linkedlist([]),
            linkedlist([1])
        )
        self.assertListEqual(
            to_list(merged),
            [1]
        ) 
    
    def test_second_empty_first_not(self): 
        merged = Solution.merge(
            linkedlist([1]),
            linkedlist([])
        )
        self.assertListEqual(
            to_list(merged),
            [1]
        ) 

    def test_one_node_each(self):
        merged = Solution.merge(
            linkedlist([1]),
            linkedlist([2])
        )
        self.assertListEqual(
            to_list(merged),
            [1, 2]
        ) 
    
    def test_three_nodes_each(self):
        merged = Solution.merge(
            linkedlist([1,3,5]),
            linkedlist([2,4,6])
        )
        self.assertListEqual(
            to_list(merged),
            [1, 2, 3, 4, 5, 6]
        ) 
    
    def test_two_nodes_four_nodes(self):
        merged = Solution.merge(
            linkedlist([1,3]),
            linkedlist([1,2,4,5])
        )
        self.assertListEqual(
            to_list(merged),
            [1,1,2,3,4,5]
        ) 

    def test_four_nodes_two_nodes(self):
        merged = Solution.merge(
            linkedlist([1,2,4,5]),
            linkedlist([1,3])
        )
        self.assertListEqual(
            to_list(merged),
            [1,1,2,3,4,5]
        )

if __name__ == '__main__':
    unittest.main()