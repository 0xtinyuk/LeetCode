class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        loc = [[-1,-1] for i in range(26)]
        for i,c in enumerate(S):
            index = ord(c)-97
            if loc[index][0]==-1:
                loc[index][0]=i
            loc[index][1]=i
        last = -1
        pool = []
        ans = []
        for i,c in enumerate(S):
            index = ord(c)-97
            if i==loc[index][0]:
                pool.append(index)
            if i==loc[index][1]:
                pool.remove(index)
            if len(pool)==0:
                ans = ans + [i-last]
                last = i
        return ans