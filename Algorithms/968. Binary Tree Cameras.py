# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        [y, n, _] = self.getMinCam(root)
        if y < n:
            return y
        return n

    def getMinCam(self, node: TreeNode) -> [int, int, int]:
        if (node.left != None) and (node.right != None):
            [ly, ln, lnc] = self.getMinCam(node.left)
            [ry, rn, rnc] = self.getMinCam(node.right)
            lt = ((ly) if (ly < ln) else ln)
            rt = ((ry) if (ry < rn) else rn)
            nc = lt + rt
            n = (ly+rt) if ((ly+rt) < (ry+lt)) else (ry+lt)
            y = (lnc if (lnc < lt) else lt) + (rnc if (rnc < rt) else rt) + 1
            return [y, n, nc]
        elif (node.left is None) and (node.right is None):
            return [1, 1, 0]
        else:
            if(node.left != None):
                [cy, cn, cnc] = self.getMinCam(node.left)
            else:
                [cy, cn, cnc] = self.getMinCam(node.right)
            nc = (cy) if (cy < cn) else cn
            n = cy
            y = (cnc if (cnc < nc) else nc)+1
            return [y, n, nc]
