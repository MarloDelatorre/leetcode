from unittest import TestCase, main

def isSubsequence(s: str, t: str) -> bool:
    s_index = 0
    for t_char in t:
        if s_index < len(s) and t_char == s[s_index]:
            s_index += 1
    return s_index == len(s)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isSubsequence("abc", "ahbgdc"))

    def test_given_case_2(self):
        self.assertFalse(isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(isSubsequence("", "asdfg"))

    def test_empty_t(self):
        self.assertFalse(isSubsequence("adf", ""))

    def test_empty_s_and_t(self):
        self.assertTrue(isSubsequence("", ""))

if __name__ == "__main__":
    main()