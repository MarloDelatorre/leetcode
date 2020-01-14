from unittest import main, TestCase

def pivotIndex(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1

class Test(TestCase):
    def test_empty_list(self):
        self.assertEqual(pivotIndex([]), -1)

    def test_single_value(self):
        self.assertEqual(pivotIndex([1]), 0)

    def test_left_edge(self):
        self.assertEqual(pivotIndex([3, 7, -4, -3]), 0)

    def test_right_edge(self):
        self.assertEqual(pivotIndex([-3, -4, 7, 3]), 3)

    def test_all_zeros(self):
        self.assertEqual(pivotIndex([0, 0, 0]), 0)

    def test_no_equal_sum(self):
        self.assertEqual(pivotIndex([1, 2, 3]), -1)

if __name__ == "__main__":
    main()