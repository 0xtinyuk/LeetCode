class Solution:
    def decodeString(self, s: str) -> str:
        s = "1["+s+"]"
        ans = ""
        stack = []
        cur = ""
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9': 
                continue
            if s[i]=='[':
                j = i-1
                while j>=0 and s[j]>='0' and s[j]<='9':
                    j-=1
                j+=1
                stack.append([int(s[j:i]),cur])
                cur = ""
                continue
            if s[i]==']':
                temp = stack.pop()
                cur = temp[1] + (cur*temp[0])
                continue
            cur = cur + s[i]
        return cur