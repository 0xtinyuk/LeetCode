class Solution {
    private String s,p;
    public boolean isMatch(String s, String p) {
        this.s=s;
        this.p=p;
        boolean[][] f=new boolean[s.length()+1][p.length()+1];
        f[0][0]=true;
        for(int i=0;i<=s.length();i++){
            for(int j=1;j<=p.length();j++){
                if(p.charAt(j-1)=='*'){
                    f[i][j]=f[i][j-1] || ((i>0)&&(f[i-1][j] || f[i-1][j-1]));
                }
                else{
                    f[i][j]=(i>0) && f[i-1][j-1] && ((p.charAt(j-1)=='?')||(p.charAt(j-1)==s.charAt(i-1)));
                }
            }
        }
        return f[s.length()][p.length()];
    }
}