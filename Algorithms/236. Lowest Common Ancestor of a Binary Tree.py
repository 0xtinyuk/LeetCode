# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father = {}
        father[root.val]=10**9+7
        b = [root]
        l = 0
        pf = False
        qf = False
        while l<len(b):
            cur = b[l]
            if cur.val == p.val:
                pf = True
            if cur.val == q.val:
                qf = True
            if pf and qf:
                break
            if cur.left:
                b.append(cur.left)
                father[cur.left.val]=cur
            if cur.right:
                b.append(cur.right)
                father[cur.right.val]=cur
            l+=1
        if pf and qf:
            p_ans = []
            q_ans = []
            cur = p
            while cur!=10**9+7:
                p_ans.append(cur)
                cur = father[cur.val]
                if cur is None:
                    return None
            cur = q
            while cur!=10**9+7:
                q_ans.append(cur)
                cur = father[cur.val]
                if cur is None:
                    return None
            if len(p_ans)==0 or len(q_ans)==0:
                return None
            pp = len(p_ans)-1
            pq = len(q_ans)-1
            while pp>=0 and pq>=0 and p_ans[pp].val==q_ans[pq].val:
                pp-=1
                pq-=1
            return p_ans[pp+1]
        return None