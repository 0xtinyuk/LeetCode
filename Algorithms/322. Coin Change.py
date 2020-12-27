class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        f = [-1 for i in range(amount+1)]
        f[0]=0
        for i in range(amount):
            if f[i]!=-1:
                for j in coins:
                    if i+j<=amount:
                        if f[i+j]==-1:
                            f[i+j]=f[i]+1
                        else:
                            f[i+j]=min(f[i+j],f[i]+1)
        return f[amount]