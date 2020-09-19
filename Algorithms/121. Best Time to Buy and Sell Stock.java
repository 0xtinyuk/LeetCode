class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length<=0) return 0;
        int ans = 0,c=prices[0];
        for (int i=1;i<prices.length;i++){
            if (prices[i]-c>ans) ans=prices[i]-c;
            if (prices[i]<c) c=prices[i];
        }
        return ans;
    }
}