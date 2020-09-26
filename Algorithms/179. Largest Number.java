class CustomSort implements Comparator<Integer> 
{ 
    public int compare(Integer a,Integer b) 
    {
        if(a==0 || b==0) return b-a;
        int ta=(int)(Math.log10(a));
        int tb=(int)(Math.log10(b));
        int ba=a/((int)(Math.pow(10,ta))),bb=b/((int)(Math.pow(10,tb)));
        while(ba==bb){
            if((ta<=0)||(tb<=0)){
                if(ta==tb) return a-b;
                if(ta<=0){
                    ta=(int)(Math.log10(a));
                    tb-=1;
                }
                else if(tb<=0) {
                    tb=(int)(Math.log10(b));
                    ta-=1;
                }
                ba=(a/((int)(Math.pow(10,ta))))%10;
                bb=(b/((int)(Math.pow(10,tb))))%10;
                continue;
            }
            ta-=1;
            tb-=1;
            ba=(a/((int)(Math.pow(10,ta))))%10;
            bb=(b/((int)(Math.pow(10,tb))))%10;
        }
        return (bb-ba);
    } 
}

class Solution {
    public String largestNumber(int[] nums) {
        if(nums.length<=0) return "";
        Integer[] sorted = new Integer[nums.length];
        for(int i=0;i<sorted.length;i++){
            sorted[i]=Integer.valueOf(nums[i]);
        }
        Arrays.sort(sorted,new CustomSort());
        String ans="";
        boolean positive=false;
        for(int i=0;i<sorted.length;i++){
            if(sorted[i]>0) positive=true;
            ans+=sorted[i];
        }
        if(!positive) return "0";
        return ans;
    }
}