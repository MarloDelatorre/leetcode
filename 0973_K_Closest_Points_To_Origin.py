from heapq import heapify, heappop
from typing import List

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist_points = [(point[0]**2 + point[1]**2, point) for point in points]
        heapify(dist_points)
        kth_closest = []
        for _ in range(K):
            _, point = heappop(dist_points)
            kth_closest.append(point)
        return kth_closest