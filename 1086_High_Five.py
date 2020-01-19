from typing import List
from heapq import heapify, heappop
from unittest import TestCase, main

def highFive(items: List[List[int]]) -> List[List[int]]:
    id_to_scores = {}
    for sid, score in items:
        if sid not in id_to_scores:
            id_to_scores[sid] = []
        id_to_scores[sid].append(score)

    top_5_averages = []
    for sid, scores in id_to_scores.items():
        heapify(scores)
        while len(scores) > 5:
            heappop(scores)
        top_5_averages.append([sid, sum(scores) // 5])

    return sorted(top_5_averages)

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            sorted(highFive([
                [1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77],
                [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]
            ])),
            sorted([[1, 87], [2, 88]])
        )

if __name__ == "__main__":
    main()