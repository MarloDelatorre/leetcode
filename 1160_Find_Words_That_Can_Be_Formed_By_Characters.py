from collections import Counter
from typing import List
from unittest import TestCase, main


def countCharacters(words: List[str], chars: str) -> int:
    letter_counter = Counter(chars)
    sum_of_lengths = 0
    for word in words:
        if word_can_be_formed(word, dict(letter_counter)):
            sum_of_lengths += len(word)
    return sum_of_lengths


def word_can_be_formed(word: str, letter_counts: dict) -> int:
    for letter in word:
        if ((count := letter_counts.get(letter, 0)) > 0):
            letter_counts[letter] = count - 1
        else:
            return False
    return True


class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(countCharacters(
            ["cat", "bt", "hat", "tree"], "atach"), 6)

    def test_given_case_2(self):
        self.assertEqual(
            countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"),
            10
        )

if __name__ == "__main__":
    main()