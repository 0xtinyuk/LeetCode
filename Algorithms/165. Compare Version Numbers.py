class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        for i in range(min(len(v1),len(v2))):
            n1=int(v1[i])
            n2=int(v2[i])
            if n1<n2:
                return -1
            if n1>n2:
                return 1
        if len(v1)==len(v2):
            return 0
        if len(v1)<len(v2):
            remaining = v2[len(v1):]
            candidate = -1
        else:
            remaining = v1[len(v2):]
            candidate = 1
        for s in remaining:
            if int(s)>0:
                return candidate
        return 0