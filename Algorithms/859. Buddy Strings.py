class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        diff = []
        x=[0 for i in range(26)]
        for i in range(len(A)):
            x[ord(A[i])-97]+=1
            if A[i]!=B[i]:
                diff.append(i)
        if len(diff)!=2:
            if len(diff)==0:
                for i in range(26):
                    if x[i]>=2:
                        return True
            return False
        if A[diff[1]]==B[diff[0]] and A[diff[0]]==B[diff[1]]:
            return True
        return False