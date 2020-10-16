class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        target = {}
        current = {}
        for c in t:
            if target.get(c) is None:
                target[c]=1
            else:
                target[c]+=1
        l = 0
        r = -1
        while r<len(s)-1:
            r+=1
            c=s[r]
            if current.get(c) is None:
                current[c]=1
            else:
                current[c]+=1
            valid = True
            for c in target.keys():
                if (current.get(c) is None) or (target[c]>current[c]):
                    valid=False
                    break
            if not valid:
                continue
            if ans=="" or r-l+1<len(ans):
                ans = s[l:r+1]
            while l<r:
                l+=1
                current[s[l-1]]-=1
                valid = True
                for c in target.keys():
                    if (current.get(c) is None) or (target[c]>current[c]):
                        valid=False
                        break
                if not valid:
                    break
                if ans=="" or r-l+1<len(ans):
                    ans = s[l:r+1]
        return ans
