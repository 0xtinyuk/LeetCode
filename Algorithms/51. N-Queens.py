class Solution:
    n=0
    cur=[]
    ans=[]
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n=n
        self.cur=[-1 for i in range(n)]
        self.ans=[]
        self.dfs(0)
        return self.ans
    
    def dfs(self,i:int):
        for j in range(self.n):
            found = False
            for k in range(i):
                if self.cur[k]==j:
                    found = True
                    break
                if abs(self.cur[k]-j)==abs(i-k):
                    found = True
                    break
            if found:
                continue
            self.cur[i]=j
            if i==(self.n-1):
                # print(self.cur)
                tmp=[]
                for k in range(self.n):
                    tmp.append("."*self.cur[k]+"Q"+"."*(self.n-self.cur[k]-1))
                self.ans.append(tmp)
                self.cur[i]=-1
                return
            self.dfs(i+1)
            self.cur[i]=-1
        return 