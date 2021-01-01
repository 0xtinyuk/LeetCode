class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        next = [0 for i in range(len(needle))]
        next = [-1] + next
        i=0
        j=-1
        while i<len(needle):
            if j==-1 or needle[i]==needle[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]
        i=0
        j=0
        while i<len(haystack) and j<len(needle):
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=next[j]
        if j==len(needle):
            return i-j
        return -1
        
        