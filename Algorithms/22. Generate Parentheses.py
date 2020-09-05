class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        if n==1:
            return ["()"]
        ans = []
        self.dfs(n,n,"",ans)
        return ans

    def dfs(self,x:int,y:int,current:str,ans:List[str]):
        if x==0 and y==0:
            ans.append(current)
            return
        if x>0:
            current = current +'('
            self.dfs(x-1,y,current,ans)
            current = current[:len(current)-1]
        if x<y:
            current = current +')'
            self.dfs(x,y-1,current,ans)
            current = current[:len(current)-1]