class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        self.A=A
        self.B=B
        self.n=len(A)
        self.candidate = []
        for i in range(self.n):
            for j in range(self.n):
                if self.B[i][j]==1:
                    self.candidate.append((i,j))
        ans = 0
        for x in range(-self.n+1,self.n):
            for y in range(-self.n+1,self.n):
                ans = max(ans,self.getOverlap(x,y))
        return ans

    
    def getOverlap(self,x:int,y:int)->int:
        # xub=min(self.n,self.n-x)
        # xlb=max(0,-x)
        # yub=min(self.n,self.n-y)
        # ylb=max(0,-y)
        # # print(xlb,xub,ylb,yub)
        counter=0
        # for i in range(xlb,xub):
        #     for j in range(ylb,yub):
        #         if self.A[i+x][j+y]==1 and self.B[i][j]==1:
        #             counter+=1
        # # print(x,y,counter)
        for i,j in self.candidate:
            if(i+x<self.n)and(i+x>=0)and(j+y<self.n)and(j+y>=0)and(self.A[i+x][j+y]==1):
                counter+=1
        return counter