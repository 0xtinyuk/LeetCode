class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if(nums.length<=0) return 0;
        int ans=0;
        int temp=nums[0],i=0;
        if(temp<k) ans+=1;
        else{
            temp=1;
            i=1;
        }
        for(int j=1;j<nums.length;j++){
            temp*=nums[j];
            while((temp>=k)&&(i<=j)){
                temp/=nums[i];
                i+=1;
            }
            if(i<=j){
                ans+=j-i+1;
            }
        }
        return ans;
    }
}