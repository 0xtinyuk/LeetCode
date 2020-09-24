class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (gas.length<=0) return -1;
        int remaining = 0,oweing = 0,start_point = 0;
        for(int i=0;i<gas.length;i++){
            remaining += gas[i] - cost[i];
            if (remaining<0){
                oweing += remaining;
                remaining = 0;
                start_point = i+1;
            }
        }
        if(remaining+oweing>=0) return start_point;
        return -1;
    }
}