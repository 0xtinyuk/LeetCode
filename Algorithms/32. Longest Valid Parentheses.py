class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        vs=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append((i,vs))
                vs=0
            else:
                if len(stack)==0:
                    vs=0
                else:
                    (start,plus) = stack.pop()
                    vs = i+1-start+plus               
                    if vs>ans:
                        ans = vs
        return ans