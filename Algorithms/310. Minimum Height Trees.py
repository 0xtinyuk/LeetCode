class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        d=[0 for i in range(n)]
        e=[[]for i in range(n)]
        for x in edges:
            e[x[0]].append(x[1])
            e[x[1]].append(x[0])
            d[x[0]]+=1
            d[x[1]]+=1
        leaves = []
        removed = [False for i in range(n)]
        remaining = n
        for i in range(n):
            if (not removed[i]) and d[i]==1:
                leaves.append(i)
                removed[i]=True
        remaining -= len(leaves)
        while remaining>2:
            new_leaves = []
            for leaf in leaves:
                for v in e[leaf]:
                    if not removed[v]:
                        d[v]-=1
                        if d[v]<=1:
                            new_leaves.append(v)
                            removed[v]=True
            leaves = new_leaves
            remaining-=len(leaves)
        ans = []
        for i in range(n):
            if not removed[i]:
                ans.append(i)
        return ans
