class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        for i in range(len(s)-9):
            tmp=s[i:i+10]
            if d.get(tmp) is None:
                d[tmp]=1
            else:
                d[tmp]+=1
        ans = []
        for (k,v) in d.items():
            if v>1:
                ans.append(k)
        return ans