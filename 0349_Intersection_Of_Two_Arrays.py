from unittest import main, TestCase

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            sorted(intersection([1, 2, 2, 1], [2, 2])),
            sorted([2])
        )

    def test_given_case_2(self):
        self.assertListEqual(
            sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])),
            sorted([9, 4])
        )

    def test_empty_non_empty(self):
        self.assertEqual(intersection([], [1, 2, 3]), [])

    def test_both_empty(self):
        self.assertEqual(intersection([], []), [])

    def test_no_intersection(self):
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6]), [])

if __name__ == "__main__":
    main()