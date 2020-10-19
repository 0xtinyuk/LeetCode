class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n=len(A)
        if n<=0:
            return -1
        candidate = {A[0],B[0]}
        for i in range(1,n):
            temp = {A[i],B[i]}
            candidate = candidate.intersection(temp)
            if len(candidate)<=0:
                return -1
        ans = n
        for x in candidate:
            counter_A=0
            counter_B=0
            for i in range(n):
                if A[i]!=x:
                    counter_A+=1
                if B[i]!=x:
                    counter_B+=1
            ans=min(ans,min(counter_A,counter_B))
        return ans
        
