from typing import List
from unittest import TestCase, main

def maxDistToClosest(seats: List[int]) -> int:
    dist = float("inf")
    for i in range(len(seats)):
        if seats[i] == 1:
            seats[i] = 0
            dist = 0
        else:
            dist += 1
            seats[i] = dist
    dist = float("inf")
    for i in range(len(seats) - 1, -1, -1):
        if seats[i] == 0:
            dist = 0
        else:
            dist += 1
            seats[i] = min(seats[i], dist)
    return max(seats) 

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)

    def test_given_case_2(self):
        self.assertEqual(maxDistToClosest([1, 0, 0, 0]), 3)

    def test_two_seats_left_taken(self):
        self.assertEqual(maxDistToClosest([1, 0]), 1)

    def test_two_seats_right_taken(self):
        self.assertEqual(maxDistToClosest([0, 1]), 1)

    def test_padded_empty_seats(self):
        self.assertEqual(maxDistToClosest([0, 0, 1, 0, 0, 1, 0, 0]), 2)

if __name__ == "__main__":
    main()