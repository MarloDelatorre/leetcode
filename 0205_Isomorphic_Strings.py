from unittest import TestCase, main

def isIsomorphic(s: str, t: str) -> bool:
    s_mappings, t_mappings = {}, {}
    for s_char, t_char in zip(s, t):
        if s_char not in s_mappings:
            s_mappings[s_char] = t_char 
        if t_char not in t_mappings:
            t_mappings[t_char] = s_char
        if s_mappings[s_char] != t_char or t_mappings[t_char] != s_char:
            return False 
    return True

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isIsomorphic("egg", "add"))

    def test_given_case_2(self):
        self.assertFalse(isIsomorphic("foo", "bar"))

    def test_given_case_3(self):
        self.assertTrue(isIsomorphic("paper", "title"))

    def test_empty_strings(self):
        self.assertTrue(isIsomorphic("", ""))

    def test_different_order_1(self):
        self.assertFalse(isIsomorphic("abba", "abab"))

    def test_different_order_2(self):
        self.assertFalse(isIsomorphic("aba", "baa"))

    def test_one_to_one(self):
        self.assertFalse(isIsomorphic("ab", "aa"))

if __name__ == "__main__":
    main()