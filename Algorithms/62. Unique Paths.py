class Solution:
    #Pascal's triangle/杨辉三角
    #ans=C(m-1)(m+n-2)
    def uniquePaths(self, m: int, n: int) -> int:
        if n < m:
            m , n = m , n
        ans = 1
        for i in range(m,m+n-1):
            ans*=i
        for i in range(1,n):
            ans=ans//i
        return ans