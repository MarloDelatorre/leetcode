from typing import List, Tuple
from unittest import TestCase, main

class MinStack:
    def __init__(self):
        self.values = []

    def push(self, x: int) -> None:
        minimum = min(self.values[-1][1], x) if self.values else x 
        self.values.append((x, minimum))

    def pop(self) -> None:
        self.values.pop()
        
    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]

class Test(TestCase):
    def test_given_case(self):
        minstack = MinStack()
        minstack.push(-2)
        minstack.push(0)
        minstack.push(-3)
        self.assertEqual(minstack.getMin(), -3)
        minstack.pop()
        self.assertEqual(minstack.top(), 0)
        self.assertEqual(minstack.getMin(), -2)

if __name__ == "__main__":
    main()