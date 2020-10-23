class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return 0
        l2 = 1
        if s[0]=="0":
            l1 = 0
        else:
            l1 = 1
        for i in range(1,len(s)):
            if s[i]!="0":
                tmp = l1
            else:
                tmp = 0
            if s[i-1]=="1":
                tmp+=l2
            if s[i-1]=="2" and ord(s[i])<=ord("6"):
                tmp+=l2
            l2 = l1
            l1=tmp
        return l1
