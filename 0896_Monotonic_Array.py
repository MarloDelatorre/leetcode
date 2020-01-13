from unittest import main, TestCase

class Solution():
    @staticmethod
    def isMonotonic(A):
        if len(A) == 1:
            return True

        non_repeating_number = A[1]
        for num in A:
            if num != A[0]:
                non_repeating_number = num
                break
        
        increasing = A[0] < non_repeating_number 
        for i in range(len(A) - 1):
            if ((increasing and A[i] > A[i + 1])
                    or (not increasing and A[i] < A[i + 1])):
                return False
        return True

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
