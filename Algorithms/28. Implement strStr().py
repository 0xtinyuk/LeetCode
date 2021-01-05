class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if len(haystack)==0:
            return -1
        next = [0 for i in range(len(needle)+1)]
        next[0]=-1
        i = 0
        j = -1
        while i<len(needle):
            if j==-1 or needle[i]==needle[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]
        i = 0 
        j = 0
        while i<len(haystack) and j<len(needle):
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j = next[j]
        if j==len(needle):
            return i-len(needle)
        return -1