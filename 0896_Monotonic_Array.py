from unittest import main, TestCase

class Solution():
    @staticmethod
    def isMonotonic(A):
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False

        return increasing or decreasing

class Test(TestCase):
    def test_true_cases(self):
        cases = [
            [1], [1, 2, 2, 3], [6, 5, 4, 4],
            [1, 2, 4, 5], [1, 1, 1], [1, 1, 1, 1, 2, 3]
        ]
        for input in cases:
            with self.subTest(input):
                self.assertTrue(Solution.isMonotonic(input))

    def test_false_cases(self):
        cases = [
            [1, 3, 2], [3, 1, 2], [2, 3, 4, 1]
        ]
        for input in cases:
            with self.subTest(input):
                self.assertFalse(Solution.isMonotonic(input))

if __name__ == "__main__":
    main()
