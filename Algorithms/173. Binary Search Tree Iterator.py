# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.traversal = []
        self.traverse(root)
        self.cur=0
    
    def traverse(self,root:TreeNode):
        if root is None:
            return
        self.traverse(root.left)
        self.traversal.append(root.val)
        self.traverse(root.right)
        return

    def next(self) -> int:
        self.cur+=1
        return self.traversal[self.cur-1]

    def hasNext(self) -> bool:
        if self.cur<len(self.traversal):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()