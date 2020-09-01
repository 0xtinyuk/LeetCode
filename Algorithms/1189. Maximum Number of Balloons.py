class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}
        for i in text:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in "balloon":
            if not (i in dic):
                dic[i] = 0
        return min(dic['b'],dic['a'],dic['l']//2,dic['o']//2,dic['n'])