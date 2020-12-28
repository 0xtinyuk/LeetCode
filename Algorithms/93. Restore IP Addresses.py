class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4:
            return []
        ans = []
        cur = ""
        def search(s: str,cur:str,i:int):
            if i==4:
                if len(s)==0:
                    ans.append(cur[1:])
                return
            if len(s)==0:
                return
            for j in range(min(3,len(s))):
                temp = s[:j+1]
                if int(temp)<=255 and str(int(temp))==temp:
                        search(s[j+1:],cur+"."+temp,i+1)
        search(s,"",0)
        return ans