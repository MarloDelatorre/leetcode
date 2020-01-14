from unittest import main, TestCase

def shortestToChar(S, C):
    distances = []
    distance = float("inf")
    for s in S:
        if s == C:
            distance = 0
        distances.append(distance)
        distance += 1
    for i in range(len(S) - 1, -1, -1):
        s = S[i]
        if s == C:
            distance = 0
        distances[i] = min(distances[i], distance)
        distance += 1
    return distances


class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            shortestToChar("loveleetcode", "e"),
            [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        )

    def test_length_one(self):
        self.assertListEqual(shortestToChar("c", "c"), [0])

    def test_all_in_s_is_c(self):
        self.assertListEqual(
            shortestToChar("ccccccccc", "c"),
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

if __name__ == "__main__":
    main()