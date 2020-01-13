from linkedlist import ListNode, to_list, to_linkedlist
from unittest import main, TestCase

class LinkedListTestCase(TestCase):
    def test_to_list_none(self):
        self.assertListEqual(to_list(None), [])

    def test_to_list_value(self):
        node = ListNode(1)
        self.assertListEqual(to_list(node), [1])

    def test_to_list_values(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        self.assertListEqual(to_list(node), [1, 2, 3])

    def test_to_linkedlist_empty(self):
        self.assertIsNone(to_linkedlist([]))

    def test_to_linkedlist_value(self):
        linkedlist = to_linkedlist([1])
        self.assertEqual(linkedlist.value, 1)

    def test_to_linkedlist_values(self):
        values = [1, 2, 3]
        linkedlist = to_linkedlist(values)
        for value in values:
            with self.subTest(value):
                self.assertEqual(linkedlist.value, value)
                linkedlist = linkedlist.next
                
if __name__ == "__main__":
    main()