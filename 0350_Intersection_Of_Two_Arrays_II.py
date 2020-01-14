from collections import Counter
from unittest import main, TestCase

def intersect(nums1, nums2):
    freq_intersection = Counter(nums1) & Counter(nums2)
    intersection = []
    for num, count in freq_intersection.items():
        for _ in range(count):
            intersection.append(num)
    return intersection

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            sorted(intersect([1, 2, 2, 1], [2, 2])),
            sorted([2, 2])
        )

    def test_given_case_2(self):
        self.assertListEqual(
            sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])),
            sorted([9, 4])
        )

    def test_empty_non_empty(self):
        self.assertEqual(intersect([], [1, 2, 3]), [])

    def test_both_empty(self):
        self.assertEqual(intersect([], []), [])

    def test_no_intersection(self):
        self.assertEqual(intersect([1, 2, 3], [4, 5, 6]), [])

if __name__ == "__main__":
    main()