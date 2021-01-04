class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        mark = [False for  i in range(n+1)]
        def work(n:int,cur):
            if len(cur)==n:
                nonlocal ans
                ans += 1
                return
            index = len(cur)+1
            for i in range(1,n+1):
                if (not mark[i]) and ((index%i==0) or (i%index==0)):
                    mark[i]=True
                    work(n,cur+[i])
                    mark[i]=False
            return
        work(n,[])
        return ans