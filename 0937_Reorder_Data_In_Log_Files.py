import unittest

class Solution():
    @staticmethod
    def reorderLogFiles(logs):
        digit_logs = []
        letter_logs = []

        for log in logs:
            _, data = log.split(" ", 1)
            if data[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def letter_log_key(log):
            identifier, data = log.split(" ", 1)
            return (data, identifier)

        letter_logs.sort(key=letter_log_key)

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