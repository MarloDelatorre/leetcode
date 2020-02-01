from collections import deque
from unittest import TestCase, main

class MyStack:
    def __init__(self):
        self.cache = None
        self.queue = deque()
        
    def push(self, x: int) -> None:
        if self.cache:
            self.queue.append(self.cache)
        self.cache = x
        
    def pop(self) -> int:
        val = self.cache
        self.cache = None
        if len(self.queue) >= 1:
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            self.cache = self.queue.popleft()
        return val
        
    def top(self) -> int:
        return self.cache
        
    def empty(self) -> bool:
        return not self.cache and len(self.queue) <= 0

class Test(TestCase):
    def test_given_case(self):
        stack = MyStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)    
        stack.push(2)
        self.assertEqual(stack.top(), 2)    
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())

    def test_pop_until_empty(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.empty())

if __name__ == "__main__":
    main()