class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        next=[-1]
        i=0
        j=-1
        while i<len(s):
            if j==-1 or s[i]==s[j]:
                i+=1
                j+=1
                next.append(j)
            else:
                j=next[j]
        d=next[len(s)]
        if d==0:
            return False
        if len(s)%(len(s)-d)==0:
            return True
        else:
            False
        