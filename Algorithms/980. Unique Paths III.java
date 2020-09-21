class Solution {
    private int ans = 0;
    private int[] dx={-1,0,1,0};
    private int[] dy={0,1,0,-1};
    private int target=2;
    public int uniquePathsIII(int[][] grid) {
        int x=0,y=0;
        for(int i=0;i<grid.length;i++)
            for(int j=0;j<grid[0].length;j++){
                if (grid[i][j]==0) this.target+=1;
                if (grid[i][j]==1){
                    x=i;
                    y=j;
                }
            }
        this.dfs(grid,1,x,y);
        return this.ans;
    }

    private void dfs(int[][] grid,int step,int x,int y){
        // System.out.println(x+" "+y+" "+step);
        if (grid[x][y]==2){
            if (step==this.target) this.ans+=1;
            return;
        }
        grid[x][y]=1;
        for(int i=0;i<4;i++){
            int nx=x+this.dx[i];
            int ny=y+this.dy[i];
            if ((nx<0) || (nx>=grid.length) || (ny<0) || (ny>=grid[0].length) 
            || (grid[nx][ny]==-1) || (grid[nx][ny]==1)) continue;
            this.dfs(grid,step+1,nx,ny);
        }
        grid[x][y]=0;
    }
}