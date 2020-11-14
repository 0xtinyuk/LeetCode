"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        self.connect(root.left)
        self.connect(root.right)
        l = root.left
        r = root.right
        while (l and r):
            l.next = r
            l = l.right
            r = r.left
        return root