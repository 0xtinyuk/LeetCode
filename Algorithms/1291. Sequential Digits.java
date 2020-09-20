class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int current = low;
        current=this.findFirst(current);
        while (current<=high){
            if ((current>=low)&&(current<=high)) ans.add(current);
            if(current%10==9) current=this.findNext(current,true);
            else current=this.findNext(current,false);
        }
        return ans;
    }
    
    private int findNext(int current,boolean moreDigits){
        if (current<10){
            if (!moreDigits){
                return current+1;
            }
            else return 12;
        }
        int second_Last = this.findNext(current / 10,moreDigits);
        int temp=(second_Last % 10)+1;
        return second_Last*10+temp;
    }

    private int findFirst(int current){
        if (current<10) return 1;
        int second_Last = this.findFirst(current / 10);
        int temp=(second_Last % 10)+1;
        return second_Last*10+temp;
    }
}