class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        digits[i]+=1
        while i>=0 and digits[i]>=10:
            digits[i]-=10
            i-=1
            if i>=0:
                digits[i]+=1
            else:
                break
        if i<0 and digits[0]==0:
            digits.insert(0,1)
        return digits