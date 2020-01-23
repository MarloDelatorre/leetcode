from typing import List
from unittest import TestCase, main

def generateParentheses(n: int) -> List[str]:
        combinations = []
        
        def generate(builder: List[str], left: int, right: int):
            nonlocal combinations
            if not left and not right:
                combinations.append("".join(builder))
                return
            
            if left > 0:
                builder.append("(")
                generate(builder, left - 1, right)
                builder.pop()
            
            if right > left:
                builder.append(")")
                generate(builder, left, right - 1)
                builder.pop()
        
        generate([], n, n)
        return combinations

class Test(TestCase):
    def test_zero_pairs(self):
        self.assertEqual(generateParentheses(0), [""])

    def test_one_pair(self):
        self.assertEqual(generateParentheses(1), ["()"])

    def test_three_pairs(self):
        self.assertEqual(
            set(generateParentheses(3)),
            set(["((()))", "(()())", "(())()", "()(())", "()()()"])
        )

if __name__ == "__main__":
    main()