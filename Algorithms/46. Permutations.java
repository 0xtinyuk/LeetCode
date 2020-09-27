class Solution {
    List<List<Integer>> ans=new ArrayList<>();
    int[] nums;
    public List<List<Integer>> permute(int[] nums) {
        this.nums=nums;
        this.find(0);
        return ans;
    }
    private void find(int index){
        if(index==this.nums.length-1) {
            List<Integer> temp = new ArrayList<Integer>(this.nums.length);
            for (int i : nums){
                temp.add(i);
            }
            this.ans.add(temp);
            return;
        }
        for(int i=index;i<this.nums.length;i++){
            this.swap(i,index);
            this.find(index+1);
            this.swap(i,index);
        }
    }
    private void swap(int i,int j){
        int t=this.nums[i];
        this.nums[i]=this.nums[j];
        this.nums[j]=t;
    }
}