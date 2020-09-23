class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int c1=0,c2=0;
        Integer n1=null,n2=null;
        for(int i=0;i<nums.length;i++){
            if((n1==null)||(n1==nums[i])){
                n1=nums[i];
                c1+=1;
            }
            else if ((n2==null)||(n2==nums[i])){
                c2+=1;
                n2=nums[i];
            }
            else if (c1==0){
                n1=nums[i];
                c1+=1;
            }
            else if (c2==0){
                n2=nums[i];
                c2+=1;
            }
            else{
                c1-=1;
                c2-=1;
            }
            // System.out.println(Integer.toString(c1)+c2);
        }
        c1=0;c2=0;
        for(int i=0;i<nums.length;i++){
            if((n1!=null)&&(n1==nums[i])) c1+=1;
            if((n2!=null)&&(n2==nums[i])) c2+=1;
        }
        List<Integer> ans=new ArrayList<Integer>();
        if(c1>nums.length/3) ans.add(n1);
        if((c2>nums.length/3)) ans.add(n2);
        return ans;
    }
}