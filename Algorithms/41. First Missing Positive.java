class Solution {
    public int firstMissingPositive(int[] nums) {
        int n=nums.length;
        for(int i=0;i<n;i++){
            if((nums[i]<=0)||(nums[i]>n)) nums[i]=n+1;
        }
        int temp=0;
        for(int i=0;i<n;i++){
            temp=Math.abs(nums[i]);
            if(temp!=n+1){
                nums[temp-1]=-Math.abs(nums[temp-1]);
            }
        }
        for(int i=0;i<n;i++)
            if(nums[i]>0) return i+1;
        return n+1;
    }
}