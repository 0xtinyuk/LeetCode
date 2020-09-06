# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1=self.DFS(root1)
        l2=self.DFS(root2)
        i=0
        j=0
        ans = []
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                ans.append(l1[i])
                i+=1
            else:
                ans.append(l2[j])
                j+=1
        if i<len(l1):
            ans = ans + l1[i:]
        if j<len(l2):
            ans = ans + l2[j:]
        # while i<len(l1):
        #     ans.append(l1[i])
        #     i+=1
        # while j<len(l2):
        #     ans.append(l2[j])
        #     j+=1
        return ans

    def DFS(self,root:TreeNode)-> List[int]:
        if root is None:
            return []
        ll=self.DFS(root.left)
        rl=self.DFS(root.right)
        ll.append(root.val)
        ll.extend(rl)
        return ll
        