from collections import Counter
from unittest import TestCase, main

def canPermutePalindrome(s: str) -> bool:
    freq = Counter(s)
    one_count = 0
    for count in freq.values():
        if count % 2 == 1:
            one_count += 1 
            
    return one_count <= 1

class Test(TestCase):
    def test_given_case_1(self):
        self.assertFalse(canPermutePalindrome("code"))

    def test_given_case_2(self):
        self.assertTrue(canPermutePalindrome("aab"))

    def test_given_case_3(self):
        self.assertTrue(canPermutePalindrome("carerac"))

    def test_empty_string(self):
        self.assertTrue(canPermutePalindrome(""))

if __name__ == "__main__":
    main()