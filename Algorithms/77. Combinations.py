class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.work(1,n,k)

    def work(self,lb:int, ub:int, k:int) -> List[List[int]]:
        ans = []
        if k==1:
            for i in range(lb,ub+1):
                ans.append([i])
            return ans
        for i in range(lb,ub-k+2):
            tmp = self.work(i+1,ub,k-1)
            for l in tmp:
                ans.append([i]+l)
        return ans