class Solution:
    memory = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        tmp = self.memory.get(s1+"|"+s2)
        if not(tmp is None):
            return tmp
        d = [0 for i in range(26)]
        for c in s1:
            d[ord(c)-97]+=1
        for c in s2:
            d[ord(c)-97]-=1
        for i in range(26):
            if d[i]!=0:
                self.memory[s1+"|"+s2]=False
                self.memory[s2+"|"+s1]=False
                return False
        for i in range(1,len(s1)):
            l1=s1[:i]
            r1=s1[i:]
            l2=s2[:i]
            r2=s2[i:]
            if self.isScramble(l1,l2) and self.isScramble(r1,r2):
                self.memory[s1+"|"+s2]=True
                self.memory[s2+"|"+s1]=True
                return True
            i=len(s1)-i
            r2=s2[:i]
            l2=s2[i:]
            if self.isScramble(l1,l2) and self.isScramble(r1,r2):
                self.memory[s1+"|"+s2]=True
                self.memory[s2+"|"+s1]=True
                return True
        self.memory[s1+"|"+s2]=False
        self.memory[s2+"|"+s1]=False
        return False

