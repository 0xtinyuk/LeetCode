class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1=set()
        s2=set()
        f1 = [0 for i in range(26)]
        f2 = [0 for i in range(26)]
        for c in word1:
            f1[ord(c)-97]+=1
            s1.add(c)
        for c in word2:
            s2.add(c)
            f2[ord(c)-97]+=1
        if len(s1)!=len(s2):
            return False
        if len(s1-s2)!=0 or len(s2-s1)!=0:
            return False
        f1 = sorted(f1)
        f2 = sorted(f2)
        for i in range(26):
            if f1[i]!=f2[i]:
                return False
        return True