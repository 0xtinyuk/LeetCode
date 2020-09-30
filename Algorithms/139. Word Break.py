class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f=[False]*(len(s)+1)
        f[0]=True
        for i in range(len(s)):
            if f[i]:
                for word in wordDict:
                    l=len(word)
                    if (i+l<=len(s)) and (word==s[i:i+l]):
                        f[i+l]=True
        return f[len(s)]

