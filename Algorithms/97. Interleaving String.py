class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        pre = [False for i in range(len(s1)+1)]
        pre[0]=True
        for i in range(len(s3)):
            cur = [False for i in range(len(s1)+1)]
            end = True
            for j in range(min(len(s1)+1,i+1)):
                if j<len(s1) and s3[i]==s1[j] and pre[j]:
                    end = False
                    cur[j+1]=True
                if (i-j<len(s2)) and s3[i]==s2[i-j] and pre[j]:
                    end = False
                    cur[j]=True
            if end:
                return False
            pre = cur
        return  pre[len(s1)]

