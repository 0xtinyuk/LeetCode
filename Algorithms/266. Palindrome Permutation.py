class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = {}
        for c in s:
            if m.get(c) is None:
                m[c]=1
            else:
                m[c]+=1
        oddN=0
        for x in m.values():
            if x%2==1:
                oddN+=1
                if oddN>1:
                    return False
        return True