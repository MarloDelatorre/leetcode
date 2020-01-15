class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children