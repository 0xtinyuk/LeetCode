class Solution:
    wordDict=[]
    memory={}
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memory={}
        if len(s)==0:
            return []
        self.wordDict=wordDict
        return self.solve(s)
    
    def solve(self,s:str)-> List[str]:
        ans=self.memory.get(s)
        if not(ans is None):
            return ans
        ans = []
        n=len(s)
        for word in self.wordDict:
            l=len(word)
            if(n-l<0):
                continue
            if(word==s[n-l:]):
                if(n-l==0):
                    ans.append(word)
                tmp=self.solve(s[:n-l])
                for x in tmp:
                    ans.append(x+" "+word)
        self.memory[s]=ans
        return ans