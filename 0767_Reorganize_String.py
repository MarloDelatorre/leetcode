from collections import Counter
from heapq import heapify, heappop, heappush 
from unittest import TestCase, main

def reorganizeString(S: str) -> str:
    heap = [(-count, letter) for letter, count in Counter(S).items()]
    reorganized = []
    heapify(heap)

    while heap:
        first_count, first_letter = heappop(heap) 

        if reorganized and reorganized[-1] == first_letter:
            return ""
        else:
            reorganized.append(first_letter)
        
        if heap:
            second_count, second_letter = heappop(heap)
            reorganized.append(second_letter)
            if second_count < -1:
                heappush(heap, (second_count + 1, second_letter))

        if first_count < -1:
            heappush(heap, (first_count + 1, first_letter))

    return "".join(reorganized)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(reorganizeString("aab"), "aba")
    
    def test_given_case_2(self):
        self.assertEqual(reorganizeString("aaab"), "")

    def test_round_robin(self):
        self.assertEqual(set(reorganizeString("aabbcccc")), set("cabcabc"))

    def test_round_robin_breaks(self):
        self.assertEqual(set(reorganizeString("vvvlo")), set("vlvov"))

if __name__ == "__main__":
    main()