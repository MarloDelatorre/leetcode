from unittest import main, TestCase

def removeDuplicates(nums):
    if not len(nums):
        return 0

    insert_index = 0
    current_num = nums[0]

    for num in nums:
        if num != current_num:
            nums[insert_index] = current_num
            insert_index += 1
            current_num = num

    if nums[insert_index] != current_num:
        nums[insert_index] = current_num 

    return insert_index + 1 

class Test(TestCase):
    def test_given_case_1(self):
        self.assert_duplicates_removed([1, 1, 2], 2)
        
    def test_given_case_2(self):
        self.assert_duplicates_removed([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)

    def test_empty_list(self):
        self.assert_duplicates_removed([], 0)

    def test_single_value_nums(self):
        self.assert_duplicates_removed([1], 1)

    def test_single_unique_value(self):
        self.assert_duplicates_removed([1, 1, 1], 1)

    def test_values_already_unique(self):
        self.assert_duplicates_removed([1, 2, 3], 3)

    def test_same_multiple_values_at_end(self):
        self.assert_duplicates_removed([1, 1, 2, 2, 3, 3, 4, 4, 4, 4], 4)

    def assert_duplicates_removed(self, nums, expected_length):
        sorted_unique_nums = sorted(list(set(nums)))
        length = removeDuplicates(nums)
        self.assertEqual(length, expected_length)
        for i in range(length):
            with self.subTest(i):
                self.assertEqual(nums[i], sorted_unique_nums[i])

if __name__ == "__main__":
    main()