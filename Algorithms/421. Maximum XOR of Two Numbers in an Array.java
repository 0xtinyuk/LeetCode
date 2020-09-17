class Solution {
    public int findMaximumXOR(int[] nums) {
        int ans = 0;
        int temp=0;
        for(int i=30;i>=0;i--){
            HashSet<Integer> candidates = new HashSet<Integer>();
            temp = temp | (1<<i);
            for(int x:nums) {
                candidates.add(x&temp);
            }
            int temp_ans = ans|(1<<i);
            for(int x:candidates){
                if (candidates.contains(temp_ans^x)){
                    ans = temp_ans;
                    break;
                }
            }
        }
        return ans;
    }
}