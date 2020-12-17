class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memory = [[False for i in range(len(s))] for j in range(len(s))]
        ans = []
        def dfs(l,cur):
            if l>=len(s):
                ans.append(cur)
            for r in range(l,len(s)):
                if (s[l]==s[r]) and ((r-l<=2) or (memory[l+1][r-1])):
                    memory[l][r]=True
                    dfs(r+1,cur+[s[l:r+1]])
        dfs(0,[])
        return ans