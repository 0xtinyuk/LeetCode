# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        q = [root]
        nl = 0
        while nl<len(q):
            l = nl
            r = len(q)-1
            nl = len(q)
            while l<=r:
                if q[l].val == u.val:
                    if l+1<=r:
                        return q[l+1]
                    else:
                        return None
                if q[l].left:
                    q.append(q[l].left)
                if q[l].right:
                    q.append(q[l].right)
                l+=1
        return None
        