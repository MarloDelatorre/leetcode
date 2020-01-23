from typing import List
from unittest import TestCase, main

primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101
]

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}

    for s in strs:
        key = hash(s)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return groups.values()

def hash_word(s: str) -> int:
    sum = 1
    
    for c in s:
        index = ord(c) - ord("a")
        sum *= primes[index]

    return sum

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            sorted([sorted(group) for group in groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])]),
            sorted([
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ])
        )

if __name__ == "__main__":
    main()