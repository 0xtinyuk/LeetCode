class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        lg10 = int(math.log10(n))
        ans = 0
        digits = sorted(digits)
        for i in range(lg10):
            ans += int(math.pow(len(digits),i+1))
        end = False
        # print(lg10)
        for i in range(lg10,-1,-1):
            cur = int((n//(math.pow(10,i)))%10)
            # print(cur)
            for j in range(len(digits)):
                x = int(digits[j])
                if x<cur:
                    ans += int(math.pow(len(digits),i))
                if x>cur:
                    end = True
                if x==cur and i==0:
                    ans += 1
                if x>=cur:
                    break
            if end or int(digits[len(digits)-1])<cur:
                break
        return ans
