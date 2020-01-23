from typing import List
from unittest import TestCase, main

def combine(n: int, k: int) -> List[List[int]]:
    if not k or k > n:
        return []

    combinations = []
    buffer = [0] * k

    def generate(index: int, start: int):
        nonlocal combinations, buffer
        if index == k:
            combinations.append(buffer[:])
            return

        for i in range(start, n + 1):
            buffer[index] = i 
            generate(index + 1, i + 1)
            
    generate(0, 1)
    return combinations

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            sorted(combine(4, 2)),
            sorted([[1, 2], [2,4], [3,4], [2,3], [1,3], [1,4]])
        )

    def test_zero_k(self):
        self.assertEqual(combine(3, 0), [])

    def test_one_n(self):
        self.assertEqual(combine(1, 1), [[1]])

    def test_multiple_n_one_k(self):
        self.assertListEqual(
            sorted(combine(4, 1)),
            [[1], [2], [3], [4]]
        )

if __name__ == "__main__":
    main()