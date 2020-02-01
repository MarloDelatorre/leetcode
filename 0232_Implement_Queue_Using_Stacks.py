from unittest import TestCase, main

class MyQueue:
    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def push(self, x: int) -> None:
        self.enqueue.append(x)

    def pop(self) -> int:
        if not self.dequeue: self._move()
        return self.dequeue.pop()

    def peek(self) -> int:
        if not self.dequeue: self._move()
        return self.dequeue[-1] 

    def empty(self) -> bool:
        return len(self.enqueue) <= 0 and len(self.dequeue) <= 0

    def _move(self) -> None:
        while self.enqueue:
            self.dequeue.append(self.enqueue.pop())

class Test(TestCase):
    def test_given_case(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)  
        self.assertEqual(queue.peek(), 1)  
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())

    def test_move_property(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        queue.push(3)
        queue.push(4)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 4)
        self.assertTrue(queue.empty())

if __name__ == "__main__":
    main()