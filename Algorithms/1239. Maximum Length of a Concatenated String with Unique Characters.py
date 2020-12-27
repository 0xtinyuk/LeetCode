class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mark = []
        for word in arr:
            s = set()
            for c in word:
                if c in s:
                    s = set()
                    break
                s.add(c)
            mark.append(s)
        ans = 0
        q = [set()]
        for i in range(len(arr)):
            temp = []
            for x in q:
                inters = x.intersection(mark[i])
                if len(inters)==0:
                    uni = x.union(mark[i])
                    temp.append(uni)
                    if len(uni)>ans:
                        ans = len(uni)       
            q = q+temp
        return ans
            
        
            