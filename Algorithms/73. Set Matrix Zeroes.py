class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return
        row=False
        col=False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0:
                        row = True
                    if j==0:
                        col = True
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0
        for i in range(1,len(matrix[0])):
            if matrix[0][i]==0:
                for j in range(1,len(matrix)):
                    matrix[j][i]=0
        if row:
            for i in range(len(matrix[0])):
                matrix[0][i]=0
        if col:
            for i in range(len(matrix)):
                matrix[i][0]=0
        return 
        