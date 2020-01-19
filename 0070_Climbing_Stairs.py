from unittest import TestCase, main

def climbStairs(n: int) -> int:
    if not n:
        return 0

    two_back, one_back = 0, 1
    for _ in range(0, n):
        two_back, one_back = one_back, one_back + two_back

    return one_back

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(climbStairs(2), 2)

    def test_given_case_2(self):
        self.assertEqual(climbStairs(3), 3)

    def test_six_steps(self):
        self.assertEqual(climbStairs(6), 13)

    def test_no_steps(self):
        self.assertEqual(climbStairs(0), 0)
        
if __name__ == "__main__":
    main()