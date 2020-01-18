from unittest import TestCase, main

def backspaceCompare(S: str, T: str) -> bool:
    return process_backspaced_string(S) == process_backspaced_string(T)

def process_backspaced_string(s: str) -> str:
    s = list(s)
    insert_index = 0
    for i in range(0, len(s)):
        if s[i] == "#":
            if insert_index > 0:
                insert_index -= 1
        else:
            s[insert_index] = s[i]
            insert_index += 1
    return "".join(s[:insert_index])

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(backspaceCompare("ab#c", "ad#c"))

    def test_given_case_2(self):
        self.assertTrue(backspaceCompare("ab##", "c#d#"))

    def test_given_case_3(self):
        self.assertTrue(backspaceCompare("a##c", "#a#c"))

    def test_given_case_4(self):
        self.assertFalse(backspaceCompare("a#c", "b"))

if __name__ == "__main__":
    main()