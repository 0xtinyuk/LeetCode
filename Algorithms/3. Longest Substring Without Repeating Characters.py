class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        l = 0
        r = 0
        result = 1
        lst = [s[l]]
        while(True):
            r += 1
            while s[r] in lst:
                lst.remove(s[l])
                l += 1
                if l >= r:
                    break
            lst.append(s[r])
            if r-l+1 > result:
                result = r-l+1
            if r == (len(s)-1):
                break

        return result
