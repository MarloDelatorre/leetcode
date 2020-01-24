from collections import Counter
from unittest import TestCase, main

def frequencySort(s: str) -> str:
    sorted_freqs = sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))
    sorted_s = []
    for char, count in sorted_freqs:
        for _ in range(count):
            sorted_s.append(char)
    return "".join(sorted_s)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(frequencySort("tree"), "eert")

    def test_given_case_2(self):
        self.assertEqual(frequencySort("cccaaa"), "aaaccc")

    def test_given_case_3(self):
        self.assertEqual(frequencySort("Aabb"), "bbAa")

if __name__ == "__main__":
    main()