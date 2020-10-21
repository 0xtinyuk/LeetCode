"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        nodes={}
        q=[node]
        ans = Node(val=node.val)
        nodes[node.val]=ans
        l=-1
        while (l<len(q)-1):
            l+=1
            current = q[l]
            new_current = nodes[current.val]
            for x in current.neighbors:
                if nodes.get(x.val) is None:
                    nodes[x.val]=Node(x.val,[])
                    q.append(x)
                new_current.neighbors.append(nodes[x.val])
        return ans