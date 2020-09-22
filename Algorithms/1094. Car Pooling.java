class CustomSort implements Comparator<int[]> 
{ 
    public int compare(int[] a,int[] b) 
    { 
        if (a[1]!=b[1]) return a[1]-b[1];
        return a[2]-b[2];
    } 
}

class CustomQueueComparator implements Comparator<int[]> 
{ 
    public int compare(int[] a,int[] b) 
    { 
        // if (a[1]!=b[1]) return a[1]-b[1];
        return a[2]-b[2];
    } 
}

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        if (trips.length<=0) return true;
        Arrays.sort(trips,new CustomSort());
        int current = 0;
        PriorityQueue<int[]> q=new PriorityQueue(10, new CustomQueueComparator());
        for(int i=0;i<trips.length;i++){
            while((q.size()>0)&&(q.peek()[2]<=trips[i][1])){
                current-=q.poll()[0];
            }
            current+=trips[i][0];
            if(current>capacity) return false;
            q.add(trips[i]);
        }
        return true;
    }
}