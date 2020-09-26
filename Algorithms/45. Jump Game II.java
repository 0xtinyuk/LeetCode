class Solution {
    public int jump(int[] nums) {
        if(nums.length<=1) return 0;
        int[] f=new int[nums.length];
        int[] q=new int[nums.length+5];
        int l=0,r=0;
        q[0]=0;
        f[0]=1;
        int ans=0x3FFFFFFF;
        if(nums[0]>=nums.length-1)
            if(f[0]<ans) return f[0];
        for(int i=1;i<nums.length;i++){
            while(q[l]+nums[q[l]]<i) l+=1;
            f[i]=f[q[l]]+1;
            if((l<=r)&&(q[r]+nums[q[r]]>=i+nums[i])) continue;
            if(i+nums[i]>=nums.length-1)
                if (f[i]<ans) ans=f[i];
            r+=1;
            q[r]=i;
        }
        if(ans==0x3FFFFFFF) ans=0;
        return ans;
    }
}