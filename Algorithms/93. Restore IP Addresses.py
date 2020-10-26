class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.work(s,1,"")
        return self.ans
        
    def work(self,s: str,i:int,ip:str):
        for j in range(min(3,len(s))):
            remaining = len(s)-j-1
            if remaining<(4-i) or remaining>(3*(4-i)):
                continue
            x = int(s[:j+1])
            if x>255:
                continue
            if j>=1 and int(s[1:j+1])==x:
                continue
            if j>=2 and int(s[2:j+1])==x:
                continue
            if i==4:
                self.ans.append(ip+s[:j+1])
            else:
                self.work(s[j+1:],i+1,ip+s[:j+1]+".")