# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return "#"
        return str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)
        """Encodes a tree to a single string.
        """
        

    def deserialize(self, data: str) -> TreeNode:
        # print(data)
        self.data = data.split(",")
        self.index=0
        return self.dfs()
        """Decodes your encoded data to tree.
        """

    def dfs(self) -> TreeNode:
        if self.index>=len(self.data) or self.data[self.index]=="#":
            self.index+=1
            return None
        # print(self.index)
        root = TreeNode(int(self.data[self.index]))
        self.index+=1
        root.left=self.dfs()
        root.right=self.dfs()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))