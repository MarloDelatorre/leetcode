from typing import List 
from unittest import TestCase

class MatrixTestCase(TestCase):
    def assert_matrix_equal(self, A, B):
        self.assertEqual(len(A), len(B))
        self.assertEqual(len(A[0]), len(B[0]))

        for row in range(len(A)):
            for col in range(len(A[0])):
                self.assertEqual(A[row][col], B[row][col])

class ListOfListsTestCase(TestCase):
    def assert_list_of_lists_equal(self, list1: List[List], list2: List[List]): 
        self.assertEqual(len(list1), len(list2))
        for sublist1, sublist2 in zip(list1, list2):
            self.assertListEqual(sublist1, sublist2)