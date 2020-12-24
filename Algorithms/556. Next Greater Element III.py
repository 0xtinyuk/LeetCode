class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        for i in range(len(s)-2,-1,-1):
            if s[i]<s[i+1]:
                candidate = i+1
                for j in range(i+2,len(s)):
                    if s[j]<s[candidate] and s[j]>s[i]:
                        candidate = j
                remaining = s[i:candidate]+s[candidate+1:]
                ans = int(s[:i]+s[candidate]+"".join(sorted(remaining)))
                if ans> ((1<<31)-1):
                    return -1
                return ans
        return -1