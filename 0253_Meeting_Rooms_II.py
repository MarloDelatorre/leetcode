from heapq import heappush, heappop
from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    heap_end_times = []
    intervals.sort(reverse=True)
    _, end_time = intervals.pop()
    heap_end_times.append(end_time)

    while intervals:
        start_time, end_time = intervals.pop()
        earliest_end_time = heappop(heap_end_times)
        if start_time < earliest_end_time:
            heappush(heap_end_times, earliest_end_time)
        heappush(heap_end_times, end_time)

    return len(heap_end_times)