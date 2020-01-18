from collections import deque
from unittest import TestCase, main

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.running_sum = 0

    def next(self, val: int) -> float:
        self.running_sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.running_sum -= self.queue.popleft()
        return self.running_sum / len(self.queue) 

class Test(TestCase):
    def test_given_case(self):
        stream = [1, 10, 3, 5]
        averages = [1, 11 / 2, 14 / 3, 6]
        moving_average = MovingAverage(3)
        for num, expected_average in zip(stream, averages):
            with self.subTest(num):
                next_average = moving_average.next(num)
                self.assertAlmostEqual(next_average, expected_average)

if __name__ == "__main__":
    main()