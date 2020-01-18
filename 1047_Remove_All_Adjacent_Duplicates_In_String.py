from unittest import TestCase, main

def removeDuplicates(S: str) -> str:
    stack = []

    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack) 

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(removeDuplicates("abbaca"), "ca")

    def test_empty_string(self):
        self.assertEqual(removeDuplicates(""), "")

    def test_even_and_odd_removals(self):
        self.assertEqual(removeDuplicates("aacdfffzx"), "cdfzx")

if __name__ == "__main__":
    main()