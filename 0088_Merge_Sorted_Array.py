import unittest

class Solution():
    @staticmethod
    def merge(nums1, m, nums2, n):
        insertion_index = m + n - 1
        index1 = m - 1
        index2 = n - 1

        while index1 >= 0 or index2 >= 0:
            if index1 < 0:
                nums1[insertion_index] = nums2[index2]
                index2 -= 1
            elif index2 < 0:
                nums1[insertion_index] = nums1[index1]
                index1 -= 1
            elif nums1[index1] > nums2[index2]:
                nums1[insertion_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[insertion_index] = nums2[index2]
                index2 -= 1 
            insertion_index -= 1
        
        return nums1

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertListEqual(
            Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3),
            [1,2,2,3,5,6]
        )
    
    def test_empty_arrays(self):
        self.assertListEqual(
            Solution.merge([], 0, [], 0),
            []
        )

    def test_first_empty_second_not(self):
        self.assertListEqual(
            Solution.merge([0], 0, [1], 1),
            [1]
        )

    def test_second_empty_first_not(self):
        self.assertListEqual(
            Solution.merge([1], 1, [], 0),
            [1]
        )

    def test_single_values(self):
        self.assertListEqual(
            Solution.merge([1, 0], 1, [2], 1),
            [1, 2]
        )

    def test_m_equals_n(self):
        self.assertListEqual(
            Solution.merge([1, 4, 7, 0, 0, 0], 3, [2, 3, 9], 3),
            [1, 2, 3, 4, 7, 9]
        )

    def test_m_less_than_n(self):
        self.assertListEqual(
            Solution.merge([1, 4, 0, 0, 0, 0], 2, [2, 3, 7, 9], 4),
            [1, 2, 3, 4, 7, 9]
        )

    def test_m_greater_than_n(self):
        self.assertListEqual(
            Solution.merge([1, 4, 7, 9, 0, 0], 4, [2, 3], 2),
            [1, 2, 3, 4, 7, 9]
        )

if __name__ == '__main__':
    unittest.main()