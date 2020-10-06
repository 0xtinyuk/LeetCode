class Solution:
    def findComplement(self, num: int) -> int:
        if num==0:
            return 1
        l2 = int(math.log(num)/math.log(2))
        if num%int(pow(2,l2))==0:
            return num-1
        return int(pow(2,(l2+1)))-num-1 