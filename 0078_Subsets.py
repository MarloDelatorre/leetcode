from typing import List
from unittest import TestCase, main

def subsets(nums: List[int]) -> List[List[int]]:
        power_set = []
        buffer = []

        def generate(index: int):
            power_set.append(buffer[:])
            
            for i in range(index, len(nums)):
                buffer.append(nums[i])
                generate(i + 1)
                buffer.pop()
        
        generate(0)
        return power_set

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            sorted(subsets([1,2 ,3])),
            sorted([
                [3], [1], [2], [1, 2, 3],
                [1, 3], [2, 3], [1, 2], []
            ])
        )

    def test_empty_case(self):
        self.assertEqual(subsets([]), [[]])

if __name__ == "__main__":
    main()