class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]
        tmp = self.grayCode(n-1)
        ans = copy.copy(tmp)
        for i in range(len(tmp)-1,-1,-1):
            ans.append(tmp[i]|(1<<(n-1)))
        return ans