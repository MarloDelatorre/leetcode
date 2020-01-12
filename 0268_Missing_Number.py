from unittest import main, TestCase

class Solution():
    @staticmethod
    def missingNumber(nums):
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(Solution.missingNumber([3, 0, 1]), 2)

    def test_given_case_2(self):
        self.assertEqual(Solution.missingNumber([9,6,4,2,3,5,7,0,1]), 8)

    def test_zero_case(self):
        self.assertEqual(Solution.missingNumber([0]), 1)

if __name__ == '__main__':
    main()