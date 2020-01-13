from unittest import main, TestCase
from collections import Counter

class Solution():
    @staticmethod
    def commonChars(A):
        freq_list = [Counter(s) for s in A]
        intersection = freq_list[0]

        for i in range(1, len(freq_list)):
            intersection &= freq_list[i]

        common_chars = []
        for letter, count in intersection.items():
           for i in range(count):
               common_chars.append(letter)

        return common_chars

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            sorted(Solution.commonChars(["bella", "label", "roller"])),
            sorted(["e", "l", "l"])
        )

    def test_given_case_2(self):
        self.assertListEqual(
            sorted(Solution.commonChars(["cool", "lock", "cook"])),
            sorted(["c", "o"])
        )

    def test_single_word(self):
        self.assertListEqual(
            sorted(Solution.commonChars(["leetcode"])),
            sorted(["l", "e", "e", "t", "c", "o", "d", "e"])
        )

if __name__ == "__main__":
    main()