import unittest

class Solution:
    @staticmethod
    def isValid(s):
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            else:
                if len(stack) <= 0 or stack.pop() != bracket_map[char]:
                    return False

        return len(stack) == 0

class Test(unittest.TestCase):
    def test_given_cases(self):
        test_cases = [
            ("()", True),
            ("()[]{}", True),
            ("(])", False),
            ("([)]", False),
            ("{[]}", True),
        ]
        for input, expected_output in test_cases:
            self.assertEqual(Solution.isValid(input), expected_output)

    def test_empty_string(self):
        self.assertTrue(Solution.isValid(""))

    def test_single_bracket(self):
        self.assertFalse(Solution.isValid("("))

if __name__ == '__main__':
    unittest.main()