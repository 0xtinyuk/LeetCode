# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = []
        can = []
        
        def find(root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
            if root is None:
                return False
            nonlocal cur,can
            cur.append(root)
            if root.val == p.val or root.val==q.val:
                if len(can)==0:
                    can = copy.deepcopy(cur)
                else:
                    return True
            if find(root.left,p,q):
                return True
            if find(root.right,p,q):
                return True
            cur.pop()
            return False
        find(root,p,q)
        for i in range(min(len(can),len(cur))):
            if can[i].val!=cur[i].val:
                return can[i-1]
        if len(can)<len(cur):
            return can[-1]
        else:
            return cur[-1]
        