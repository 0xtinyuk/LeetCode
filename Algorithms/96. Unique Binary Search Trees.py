class Solution:
    def numTrees(self, n: int) -> int:
        self.mem = {}
        if n<=0:
            return 0
        return self.search(1,n)

    def search(self,l:int,r:int)->int:
        if l>r:
            return 1
        if l==r:
            return 1
        ans = self.mem.get(str(l)+"->"+str(r))
        if ans is None:
            ans = 0
            for i in range(l,r+1):
                tmp_l = self.search(l,i-1)
                tmp_r = self.search(i+1,r)
                ans+=tmp_l*tmp_r
                # for ls in tmp_l:
                #     for rs in tmp_r:
                #         ans.append(TreeNode(i,ls,rs))
            self.mem[str(l)+"->"+str(r)] = ans
        return ans    