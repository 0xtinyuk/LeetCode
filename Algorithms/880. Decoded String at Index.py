class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        l=0
        for c in S:
            if ord(c)>=ord('0') and ord(c)<=ord('9'):
                l*=ord(c)-ord('0')
            else:
                l+=1
        for i in range(len(S)-1,-1,-1):
            K%=l
            c=S[i]
            if K==0 and (not(ord(c)>=ord('0') and ord(c)<=ord('9'))):
                return c
            if ord(c)>=ord('0') and ord(c)<=ord('9'):
                l/=ord(c)-ord('0')
            else:
                l-=1