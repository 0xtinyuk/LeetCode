/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    static int r[2]={0,0};
    for(int i=0;i<numsSize-1;i++)
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                r[0]=i;
                r[1]=j;
                return r;
            }
        }
    return r;
}