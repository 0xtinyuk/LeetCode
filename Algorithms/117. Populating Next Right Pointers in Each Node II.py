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
        ne = self.getLeftInNextLevel(root.next)
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = ne
        if root.right:
            root.right.next = ne
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        return root     
    
    def getLeftInNextLevel(self,root:'Node') -> 'Node':
        if root is None:
            return None
        if root.left:
            return root.left
        if root.right:
            return root.right
        return self.getLeftInNextLevel(root.next)