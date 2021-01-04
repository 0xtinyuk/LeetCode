class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        x = m-1
        y = 0
        while x>=0 and x<m and y>=0 and y<n:
            if matrix[x][y]==target:
                return True
            if matrix[x][y]<target:
                y+=1
            else:
                x-=1
        return False