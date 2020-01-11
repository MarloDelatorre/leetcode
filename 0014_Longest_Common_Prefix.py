from unittest import TestCase, main

class Solution():
    @staticmethod
    def longestCommonPrefix(strs):
        if not strs:
            return ""

        end_index = 0
        for letters in zip(*strs):
            if letters.count(letters[0]) == len(letters):
                end_index += 1
            else:
                break

        return strs[0][:end_index]

class Test(TestCase):
    def test_given_cases(self):
        cases = [
            (["flower","flow","flight"], "fl"),
            (["dog","racecar","car"], "")
        ]

        for value, expected in cases:
            with self.subTest(value):
                self.assertEqual(Solution.longestCommonPrefix(value), expected)

    def test_empty_case(self):
        self.assertEqual(Solution.longestCommonPrefix([]), "")

if __name__ == "__main__":
    main()