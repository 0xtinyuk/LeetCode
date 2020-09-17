class Solution {
    public String countAndSay(int n) {
        if (n==1) return "1";
        String last=this.countAndSay(n-1);
        int counter=1;
        char lch=last.charAt(0);
        String ans="";
        for (int i=1;i<last.length();i++){
            char ch=last.charAt(i);
            if (ch==lch){
                counter++;
            }
            else{
                ans = ans+(char)(counter+48)+lch;
                counter=1;
                lch=ch;
            }
        }
        ans = ans+(char)(counter+48)+lch;
        return ans;
    }
}