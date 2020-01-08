import unittest

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @staticmethod
    def to_list(linked_list):
        list_repr = []

        while linked_list is not None:
            list_repr.append(linked_list.val)
            linked_list = linked_list.next

        return list_repr
    
    @staticmethod
    def from_list(list_repr):
        sentinel = ListNode(None)
        tail = sentinel

        for element in list_repr:
            tail.next = ListNode(element)
            tail = tail.next

        return sentinel.next

class Solution():
    @staticmethod
    def merge(list1, list2):
        sentinel = ListNode(None)
        tail = sentinel

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
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
        list1 = ListNode.from_list([1,2,4])
        list2 = ListNode.from_list([1,3,4])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1,1,2,3,4,4]
        )

    def test_empty_case(self):
        list1 = ListNode.from_list([])
        list2 = ListNode.from_list([])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            []
        )

    def test_one_empty_one_not(self):
        list1 = ListNode.from_list([1])
        list2 = ListNode.from_list([])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1]
        ) 

        list3 = ListNode.from_list([])
        list4 = ListNode.from_list([1])
        actual = Solution.merge(list3, list4)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1]
        ) 

    def test_one_node_each(self):
        list1 = ListNode.from_list([1])
        list2 = ListNode.from_list([2])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1, 2]
        ) 
    
    def test_three_nodes_each(self):
        list1 = ListNode.from_list([1,3,5])
        list2 = ListNode.from_list([2,4,6])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1, 2, 3, 4, 5, 6]
        ) 
    
    def test_two_nodes_four_nodes(self):
        list1 = ListNode.from_list([1,3])
        list2 = ListNode.from_list([1,2,4,5])
        actual = Solution.merge(list1, list2)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1,1,2,3,4,5]
        ) 

        list3 = ListNode.from_list([1,2,4,5])
        list4 = ListNode.from_list([1,3])
        actual = Solution.merge(list3, list4)
        self.assertListEqual(
            ListNode.to_list(actual),
            [1,1,2,3,4,5]
        )
if __name__ == '__main__':
    unittest.main()