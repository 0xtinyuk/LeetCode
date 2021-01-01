class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l = 0
        r = len(S)-1
        S = list(S)
        while l<r:
            while l<len(S) and (ord(S[l])<65 or ord(S[l])>ord('z') or (ord(S[l])>ord('Z') and ord(S[l])<ord('a'))):
                l+=1
            while r>=0 and (ord(S[r])<65 or ord(S[r])>ord('z') or (ord(S[r])>ord('Z') and ord(S[r])<ord('a'))):
                r-=1
            if l<r:
                c = S[l]
                S[l]=S[r]
                S[r]=c
                l+=1
                r-=1
        return "".join(S)