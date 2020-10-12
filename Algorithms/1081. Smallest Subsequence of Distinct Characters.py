class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = [-1 for i in range(26)]
        added = [False for i in range(26)]
        for i in range(len(s)):
            last[ord(s[i])-97] = i
        res = []
        for i in range(len(s)):
            if added[ord(s[i])-97]:
                continue
            while (not len(res)==0) and ((res[len(res)-1]>s[i]) and last[ord(res[len(res)-1])-97]>i):
                added[ord(res[len(res)-1])-97]=False
                res.pop(len(res)-1)
            added[ord(s[i])-97]=True
            res.append(s[i])
        ans = ""
        for l in res:
            ans += l[0]
        return ans