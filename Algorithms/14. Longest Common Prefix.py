class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        ans = strs[0]
        for i in range(1,len(strs)):
            ans = self.getLCP(ans,strs[i])
            if len(ans)==0:
                return ""
        return ans

    def getLCP(self,s1:str,s2:str)-> str:
        if len(s1)>len(s2):
            s1,s2=s2,s1
        LCP=""
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return LCP
            LCP = LCP + s1[i]
        return LCP

        