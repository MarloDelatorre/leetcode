from typing import Callable 
from unittest import TestCase, main

def isBadVersionGenerator(first_bad_version: int) -> bool:
    def isBadVersion(version: int) -> bool:
        return version >= first_bad_version
    return isBadVersion

def firstBadVersion(n: int, isBadVersion: Callable[[int], bool]) -> bool:
    left, right = 1, n
        
    while left < right:
        mid = left // 2 + right // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(firstBadVersion(5, isBadVersionGenerator(4)), 4)

    def test_single_bad_version(self):
        self.assertEqual(firstBadVersion(1, isBadVersionGenerator(1)), 1)

    def test_bad_version_first_half(self):
        self.assertEqual(firstBadVersion(9, isBadVersionGenerator(3)), 3)

    def test_bad_version_second_half(self):
        self.assertEqual(firstBadVersion(9, isBadVersionGenerator(8)), 8)

if __name__ == "__main__":
    main()