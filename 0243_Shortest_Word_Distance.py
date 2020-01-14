from unittest import main, TestCase

def shortestDistance(words, word1, word2):
    word_to_index = {}
    distance = float("inf")
    for i, word in enumerate(words):
        word_to_index[word] = i
        if word == word1:
            distance = min(
                distance,
                i - word_to_index.get(word2, float("-inf"))
            )
        elif word == word2:
            distance = min(
                distance,
                i - word_to_index.get(word1, float("-inf"))
            )
    return distance

class Test(TestCase):
    @classmethod
    def setUpClass(self):
        self.words = ["practice", "makes", "perfect", "coding", "makes"]

    def test_given_case_1(self):
        self.assertEqual(shortestDistance(self.words, "coding", "practice"), 3)

    def test_given_case_2(self):
        self.assertEqual(shortestDistance(self.words, "makes", "coding"), 1)

    def test_adjacent_words(self):
        self.assertEqual(shortestDistance(self.words, "practice", "makes"), 1)

if __name__ == "__main__":
    main()