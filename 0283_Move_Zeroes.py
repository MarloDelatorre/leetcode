import unittest

class Solution():
    @staticmethod
    def moveZeroes(nums):
        insert_index = 0
        for num in nums:
            if num != 0:
                nums[insert_index] = num
                insert_index += 1

        while insert_index < len(nums):
            nums[insert_index] = 0
            insert_index += 1

        return nums

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertListEqual(
            Solution.moveZeroes([0, 1, 0, 3, 12]),
            [1, 3, 12, 0, 0]
        )

    def test_empty_list(self):
        self.assertListEqual(
            Solution.moveZeroes([]),
            []
        )

    def test_single_value(self):
        self.assertListEqual(
            Solution.moveZeroes([1]),
            [1]
        )
    
    def test_zeroes_at_start(self):
        self.assertListEqual(
            Solution.moveZeroes([0, 0, 0, 1]),
            [1, 0, 0, 0]
        )

    def test_zeroes_at_end(self):
        self.assertListEqual(
            Solution.moveZeroes([1, 2, 0, 0, 0]),
            [1, 2, 0, 0, 0]
        )

    def test_alternating_zeroes(self):
        self.assertListEqual(
            Solution.moveZeroes([0, 1, 0, 2, 0, 3, 0]),
            [1, 2, 3, 0, 0, 0, 0]
        )
    
    def test_all_zeroes(self):
        self.assertListEqual(
            Solution.moveZeroes([0, 0, 0, 0]),
            [0, 0, 0, 0]
        )

    def test_all_non_zero(self):
        self.assertListEqual(
            Solution.moveZeroes([1, 2, 3, 4]),
            [1, 2, 3, 4]
        )

if __name__ == '__main__':
    unittest.main()