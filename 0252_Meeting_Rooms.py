from typing import List
from unittest import TestCase, main

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda interval: interval[0])
    for i in range(1, len(intervals)):
        _, prev_end = intervals[i - 1]
        curr_start, _ = intervals[i]
        if curr_start < prev_end:
            return False
    return True

class Test(TestCase):
    def test_given_case_1(self):
        self.assertFalse(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))

    def test_given_case_2(self):
        self.assertTrue(canAttendMeetings([[7, 10], [2, 4]]))

    def test_empty_list(self):
        self.assertTrue(canAttendMeetings([]))

    def test_no_overlaps(self):
        self.assertTrue(canAttendMeetings([[0, 5], [20, 25], [10, 15]]))

    def test_overlap_first_and_last(self):
        self.assertFalse(canAttendMeetings([[0, 10], [15, 20], [5, 25]]))

if __name__ == "__main__":
    main()