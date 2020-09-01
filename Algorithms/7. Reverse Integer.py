class Solution:
    def reverse(self, x: int) -> int:
        result = ""
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(-x)[::-1])
        if result.bit_length() < 32:
            return result
        return 0
