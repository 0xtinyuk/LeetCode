class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in c:
            for j in range(len(matrix)):
                matrix[j][i]=0
        return
        