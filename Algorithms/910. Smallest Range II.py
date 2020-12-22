class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A=sorted(A)
        ans = A[-1]-A[0]
        ma=A[-1]-K
        mi=A[0]+K
        for i in range(len(A)-1):
            tma=max(max(ma,A[i]+K),A[i+1]-K)
            tmi=min(min(mi,A[i]+K),A[i+1]-K)
            ans = min(ans,tma-tmi)
        return ans