# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        self.mem = {}
        if n<=0:
            return []
        return self.search(1,n)

    def search(self,l:int,r:int)->List[TreeNode]:
        if l>r:
            return [None]
        if l==r:
            return [TreeNode(l)]
        ans = self.mem.get(str(l)+"->"+str(r))
        if ans is None:
            ans = []
            for i in range(l,r+1):
                tmp_l = self.search(l,i-1)
                tmp_r = self.search(i+1,r)
                for ls in tmp_l:
                    for rs in tmp_r:
                        ans.append(TreeNode(i,ls,rs))
            self.mem[str(l)+"->"+str(r)] = ans
        return ans