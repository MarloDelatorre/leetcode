from collections import Counter
from heapq import _heapify_max, _heappop_max
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    _heapify_max(heap := Counter(nums).items())
    most_freq = []
    for _ in range(k - 1):
        most_freq.append(_heappop_max(heap))
    return most_freq
