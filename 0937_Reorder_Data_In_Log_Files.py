import unittest
from operator import attrgetter

class Log():
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data

    def __repr__(self):
        return f"{self.identifier} {self.data}"

class Solution():
    @staticmethod
    def reorderLogFiles(logs):
        digit_logs = []
        letter_logs = []

        for log in logs:
            identifier, *data = log.split()
            if data[0].isalpha():
                letter_logs.append(Log(identifier, " ".join(data)))
            else:
                digit_logs.append(log)
            
        letter_logs.sort(key=attrgetter('data', 'identifier'))
        letter_logs = [repr(log) for log in letter_logs]
        
        return letter_logs + digit_logs

class Test(unittest.TestCase):
    def test_given_case(self):
        self.assertListEqual(
            Solution.reorderLogFiles([
                "dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                "let2 own kit dig", "let3 art zero"
            ]),
            [
                "let1 art can", "let3 art zero", "let2 own kit dig",
                "dig1 8 1 5 1", "dig2 3 6"
            ]
        )

    def test_empty_logs(self):
        self.assertListEqual(Solution.reorderLogFiles([]), [])

    def test_stable_ordering(self):
        self.assertListEqual(
            Solution.reorderLogFiles(["a2 3 4", "a3 dog cat", "a1 1 2"]),
            ["a3 dog cat", "a2 3 4", "a1 1 2"] 
        )

    def test_tie_breaker(self):
        self.assertListEqual(
            Solution.reorderLogFiles(["a2 dog cat", "a1 dog cat", "a3 1 2"]),
            ["a1 dog cat", "a2 dog cat", "a3 1 2"]
        )

    def test_letters_after_digits(self):
        self.assertListEqual(
            Solution.reorderLogFiles(["a2 dog cat", "a1 1 2", "a3 cat dog", "a5 6 7"]),
            ["a3 cat dog", "a2 dog cat", "a1 1 2", "a5 6 7"]
        )

if __name__ == '__main__':
    unittest.main()