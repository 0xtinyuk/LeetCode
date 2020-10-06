class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:
            return 1
        l2 = int(math.log(N)/math.log(2))
        if N%int(pow(2,l2))==0:
            return N-1
        return int(pow(2,(l2+1)))-N-1      