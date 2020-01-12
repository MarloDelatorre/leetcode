import re
from collections import Counter
from unittest import main, TestCase

class Solution():
    @staticmethod
    def mostCommonWord(paragraph, banned):
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return Counter([word for word in words if word not in banned_set]).most_common(1)[0][0]

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            Solution.mostCommonWord(
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                ["hit"]
            ),
            "ball"
        )

    def test_no_banned_words(self):
        self.assertEqual(
            Solution.mostCommonWord(
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                []
            ),
            "hit"
        )

if __name__ == '__main__':
    main()
