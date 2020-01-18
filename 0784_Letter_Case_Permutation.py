from typing import List
from unittest import TestCase, main

def letterCasePermutation(S: str) -> List[str]:
    permutations = []

    def create_permutation(index: int, builder: str):
        nonlocal S
        while index < len(S) and not S[index].isalpha():
            builder += S[index]
            index += 1
        if index >= len(S):
            nonlocal permutations
            permutations.append(builder)
        else:
            create_permutation(index + 1, builder + S[index].lower())
            create_permutation(index + 1, builder + S[index].upper())
    create_permutation(0, "")

    return permutations

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(
            set(letterCasePermutation("a1b2")),
            set(["a1b2", "a1B2", "A1b2", "A1B2"])
        )

    def test_given_case_2(self):
        self.assertEqual(
            set(letterCasePermutation("3z4")),
            set(["3z4", "3Z4"])
        )

    def test_given_case_3(self):
        self.assertListEqual(
            letterCasePermutation("12345"),
            ["12345"]
        )

    def test_empty_string(self):
        self.assertEqual(letterCasePermutation(""), [""])

if __name__ == "__main__":
    main()