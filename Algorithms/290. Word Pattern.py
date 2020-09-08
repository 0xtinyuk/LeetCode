class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dict = {}
        pa=["" for i in range(26)]
        i=-1
        strlist = str.split()
        for s in strlist:
            i+=1
            if i>=len(pattern):
                return False
            id = ord(pattern[i])-97
            if (pa[id]==""):
                pa[id]=s
            if dict.get(s) is None:
                dict[s]=id
            if (pa[id]!=s) or (dict[s]!=id):
                return False
        if i<len(pattern)-1:
            return False
        return True      