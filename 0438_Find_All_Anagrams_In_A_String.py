from typing import List
from unittest import TestCase, main

primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101
]

def findAnagrams(s: str, p: str) -> List[int]:
    indices = []
    
    p_hash = 1
    for c in p:
        p_hash *= primes[ord(c) - ord('a')]
    
    s_hash = 1
    for i, c in enumerate(s):
        s_hash *= primes[ord(c) - ord('a')]
        if i >= len(p):
            s_hash //= primes[ord(s[i - len(p)]) - ord('a')]
        if s_hash == p_hash:
            indices.append(i - len(p) + 1)
            
    return indices

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            findAnagrams("cbaebabacd", "abc"),
            [0, 6]
        )

    def test_given_case_2(self):
        self.assertListEqual(
            findAnagrams("abab", "ab"),
            [0, 1, 2]
        )

    def test_duplicate_in_p(self):
        self.assertListEqual(
            findAnagrams("ababa", "aba"),
            [0, 2]
        )

if __name__ == "__main__":
    main()