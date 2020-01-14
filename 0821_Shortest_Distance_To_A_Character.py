from unittest import main, TestCase

def shortestToChar(S, C):
    distances = [0] * len(S)
    c_index = S.find(C) 
    for _ in range(c_index, len(S)):
        for left in range(c_index - 1, -1, -1):
            distance = c_index - left
            if S[left] == C or 0 < distances[left] <= distance:
                break
            distances[left] = distance 
        for right in range(c_index + 1, len(S), 1):
            distance = right - c_index 
            if S[right] == C:
                c_index = right
                break
            distances[right] = distance
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