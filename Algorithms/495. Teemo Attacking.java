class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        long ans = duration*timeSeries.length;
        for(int i=1;i<timeSeries.length;i++){
            if(timeSeries[i]-timeSeries[i-1]<duration){
                ans-=duration-timeSeries[i]+timeSeries[i-1];
            }
        }
        return (int)ans;
    }
}