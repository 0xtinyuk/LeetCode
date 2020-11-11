class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A)<=0:
            return A
        for x in A:
            x.reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j]=1-A[i][j]
        return A