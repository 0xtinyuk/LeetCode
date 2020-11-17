class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans = 0
        asc = 0
        dec = 0
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                asc = 0
                dec = 0
                continue
            if A[i]>A[i-1]:
                if dec!=0:
                    asc = 0
                    dec = 0
                asc +=1
            else:
                dec+=1
                if (asc>0)and(asc+dec+1>ans):
                    ans = asc+dec+1
        return ans