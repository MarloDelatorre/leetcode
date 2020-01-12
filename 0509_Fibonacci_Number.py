from unittest import main, TestCase

class Solution():
    @staticmethod
    def fib(n):
        if n < 0:
            raise Exception("Fibonacci sequence is not defined for negative numbers")
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a = b = 1
        for _ in range(2, n):
            a, b = a + b, a
        return a

class Test(TestCase):
    def test_given_cases(self):
        cases = [
            (2, 1),
            (3, 2),
            (4, 3)
        ]

        for input, expected in cases:
            with self.subTest(input):
                self.assertEqual(Solution.fib(input), expected)

    def test_zero_case(self):
        self.assertEqual(Solution.fib(0), 0)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            Solution.fib(-1)

if __name__ == "__main__":
    main()