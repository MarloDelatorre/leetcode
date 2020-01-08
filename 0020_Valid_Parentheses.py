import unittest

class Solution:
    @staticmethod
    def isValid(s):
        stack = []
        open_brackets = set("([{")
        
        for char in s:
            length = len(stack)
            if char in open_brackets:
                stack.append(char)
            elif char == ')':
                if length == 0 or stack.pop() != '(':
                    return False
            elif char == ']':
                if length == 0 or stack.pop() != '[':
                    return False
            elif char == '}':
                if length == 0 or stack.pop() != '{':
                    return False
            else:
                raise Exception('Unexpected character given')

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
            actual = Solution.isValid(input)
            self.assertEqual(actual, expected_output)

    def test_empty_string(self):
        self.assertTrue(Solution.isValid(""))

    def test_single_bracket(self):
        self.assertFalse(Solution.isValid("("))

if __name__ == '__main__':
    unittest.main()