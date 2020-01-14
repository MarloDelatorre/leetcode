from linkedlist import ListNode, linkedlist, to_list
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

    def test_linkedlist_empty(self):
        self.assertIsNone(linkedlist([]))

    def test_linkedlist_value(self):
        links = linkedlist([1])
        self.assertEqual(links.value, 1)

    def test_linkedlist_values(self):
        values = [1, 2, 3]
        links = linkedlist(values)
        for value in values:
            with self.subTest(value):
                self.assertEqual(links.value, value)
                links = links.next
                
if __name__ == "__main__":
    main()