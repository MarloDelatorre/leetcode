from unittest import TestCase, main

def reverseWords(s: str) -> str:
    return " ".join([word[::-1] for word in s.split(' ')])

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            reverseWords("Let's take LeetCode contest"),
            "s'teL ekat edoCteeL tsetnoc"
        )

    def test_empty_string(self):
        self.assertEqual(reverseWords(""), "")

    def test_one_word(self):
        self.assertEqual(reverseWords("Leetcode"), "edocteeL")

if __name__ == "__main__":
    main()