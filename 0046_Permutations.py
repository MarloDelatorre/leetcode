from typing import List
from unittest import TestCase, main

def permute(nums: List[int]) -> List[List[int]]:
    if not len(nums):
        return []

    permutations = []
    buffer = []
    used = set()

    def generate(index):
        nonlocal permutations, buffer, used 

        if index == len(nums):
            permutations.append(buffer[:])
            return

        for num in nums:
            if num not in used:
                used.add(num)
                buffer.append(num)
                generate(index + 1)
                buffer.pop()
                used.remove(num)

    generate(0)
    return permutations

class Test(TestCase):
    def test_empty_set(self):
        self.assertEqual(permute([]), [])

    def test_single_number(self):
        self.assertEqual(permute([1]), [[1]])

    def test_multiple_nums(self):
        self.assertEqual(
            sorted(permute([1, 2, 3])),
            sorted([
                [1,2,3], [1,3,2], [2,1,3],
                [2,3,1], [3,1,2], [3,2,1]
            ])
        )

if __name__ == "__main__":
    main()