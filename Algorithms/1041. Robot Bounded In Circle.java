class Solution {
    public boolean isRobotBounded(String instructions) {
        int[] dx={0,1,0,-1},dy={1,0,-1,0};
        int x=0,y=0,f=0;
        for(int i=0;i<instructions.length();i++){
            char ch=instructions.charAt(i);
            if (ch=='G'){
                x+=dx[f];y+=dy[f];
            }
            else if(ch=='L'){
                f=(f-1)<0?3-(-f)%4:(f-1)%4;
                // System.out.println(f);
            }
            else{
                f=(f+1)%4;
            }
        }
        if(x==0 && y==0) return true;
        if(f!=0) return true;
        return false;
    }
}