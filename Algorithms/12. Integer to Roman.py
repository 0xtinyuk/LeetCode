class Solution:
    def intToRoman(self, num: int) -> str:
        list = [[1000,'M'],[500,'D'],[100,'C'],[50,'L'],[10,'X'],[5,'V'],[1,'I']]
        ans = ""
        for i in range(0,len(list),2):
            if num >= list[i][0]:
                ans = ans + list[i][1]*(num//list[i][0])
                num = num-  (num// list[i][0])*list[i][0]
            if i+2<len(list):
                current = list[i][0]-list[i+2][0]
                if num >= current:
                    ans = ans + list[i+2][1]+list[i][1]
                    num = num -current
            if i+1<len(list):
                current = list[i+1][0]
                if num >= current:
                    ans = ans + list[i+1][1]
                    num = num -current
                if i+2<len(list):
                    current = list[i+1][0]-list[i+2][0]
                    if num >= current:
                        ans = ans + list[i+2][1]+list[i+1][1]
                        num = num -current
        return ans