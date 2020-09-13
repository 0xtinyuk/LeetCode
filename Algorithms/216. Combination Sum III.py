class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k==0:
            return []
        mark=[False for i in range(10)]
        ans = self.dfs(mark,k,n,0)
        return ans
    
    def dfs(self,mark:List[bool],k_left:int,n_left:int,lb:int) -> List[List[int]]:
        if k_left == 1:
            if n_left<10 and (not mark[n_left]) and n_left>lb:
                return [[n_left]]
            return []
        ans = []
        for i in range(lb+1,min(n_left,10)):
            if not mark[i]:
                mark[i]=True
                temp=self.dfs(mark,k_left-1,n_left-i,i)
                for x in range(len(temp)):
                    temp[x].insert(0,i)
                ans.extend(temp)
                mark[i]=False
        return ans
            