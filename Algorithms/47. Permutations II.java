class Solution {
    List<List<Integer>> ans=new ArrayList<>();
    ArrayList<Integer> current=new ArrayList<>();
    boolean[] visited;
    int[] nums;
    public List<List<Integer>> permuteUnique(int[] nums) {
        this.nums=nums;
        Arrays.sort(this.nums);
        this.visited=new boolean[this.nums.length];
        this.dfs();
        return ans;
    }
    public void dfs(){
        if(current.size()==this.nums.length){
            ans.add(new ArrayList(current));
            return;
        }
        for(int i=0;i<this.nums.length;i++){
            if(this.visited[i]) continue;
            if((i>0)&&(this.nums[i]==this.nums[i-1])&&(!this.visited[i-1])) continue;
            this.visited[i]=true;
            current.add(this.nums[i]);
            this.dfs();
            current.remove(current.size()-1);
            this.visited[i]=false;
        }
    }
}