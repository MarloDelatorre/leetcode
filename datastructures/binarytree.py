from collections import deque
from typing import Iterable, List

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def to_list(node: TreeNode) -> List:
    values = []
    queue = deque()
    if node is not None:
        queue.append(node)
    while queue:
        popped = queue.popleft()
        if popped is None:
            values.append(None)
        else:
            queue.append(popped.left)
            queue.append(popped.right)
            values.append(popped.val)
    while values and values[-1] is None:
        values.pop()
    return values

def binarytree(values: Iterable) -> TreeNode:
    if not len(values):
        return None 
    queue = deque()
    index = 1
    root = TreeNode(values[0])

    queue.append(root)

    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()

            for j in range(index, min(index + 2, len(values))):
                if values[j] is None:
                    if j % 2 == 1:
                        curr.left = None
                    else:
                        curr.right = None
                else:
                    next = TreeNode(values[j])
                    queue.append(next)
                    if j % 2 == 1:
                        curr.left = next
                    else:
                        curr.right = next
            index += 2

    return root