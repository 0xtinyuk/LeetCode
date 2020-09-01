class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows==1:
            return s
        ans = ""
        round_length = numRows + numRows-2
        for i in range(numRows):
            shifting = 0
            while shifting+i<len(s):
                ans = ans + s[shifting+i]
                if i!=0 and i!=numRows-1:
                    if shifting+round_length-i<len(s):
                        ans = ans + s[shifting+round_length-i]
                shifting +=round_length
        return ans
        