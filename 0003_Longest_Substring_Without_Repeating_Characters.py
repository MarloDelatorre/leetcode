from unittest import TestCase, main

def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    tail_index = max_count = count = 0
    
    for c in s:
        if c in seen:
            while c in seen:
                seen.remove(s[tail_index])
                tail_index += 1
                count -= 1
        seen.add(c)
        count += 1
        max_count = max(max_count, count)
    
    return max_count

class Test(TestCase):
    def test_given_cases(self):
        cases = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
        for input, actual in cases:
            with self.subTest(f"s=\"{input}\""):
                self.assertEqual(lengthOfLongestSubstring(input), actual)

if __name__ == "__main__":
    main()