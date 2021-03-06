class Solution {
    int[] candidates;
    List<List<Integer>> ans=new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        this.candidates=candidates;
        this.dfs(target,0,new ArrayList<Integer>());
        return this.ans;
    }

    private void dfs(int target, int index, ArrayList<Integer> current){
        for(int i=index;i<this.candidates.length;i++){
            if (target<this.candidates[i]) return;
            if (target==this.candidates[i]){
                current.add(target);
                this.ans.add(new ArrayList<Integer>(current));
                // System.out.println(ans);
                current.remove(current.size()-1);
                return;
            }
            current.add(this.candidates[i]);
            this.dfs(target-this.candidates[i],i,current);
            current.remove(current.size()-1);
        }
        return;
    }
}