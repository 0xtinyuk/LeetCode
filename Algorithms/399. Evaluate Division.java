class Solution {
    class Edge {
        public String t;
        public Double v;

        public Edge(String t, Double v) {
            this.t = t;
            this.v = v;
        }
    }

    HashMap<String,ArrayList<Edge>> map = new HashMap<>();
    HashSet<String> current;
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for(int i=0;i<values.length;i++){
            String xs=equations.get(i).get(0);
            String ys=equations.get(i).get(1);
            if(!map.containsKey(xs)){
                map.put(xs,new ArrayList<>());
            }
            map.get(xs).add(new Edge(ys,values[i]));
            if(!map.containsKey(ys)){
                map.put(ys,new ArrayList<>());
            }
            map.get(ys).add(new Edge(xs,1/values[i]));
        }
        double[] ans=new double[queries.size()];
        for(int i=0;i<queries.size();i++){
            String xs=queries.get(i).get(0);
            String ys=queries.get(i).get(1);
            this.current=new HashSet<>();
            ans[i]=this.dfs(xs,ys);
        }
        return ans;
    }

    public double dfs(String s,String t){
        if(!this.map.containsKey(s)) return -1;
        if(!this.map.containsKey(t)) return -1;
        if(s.equals(t)) return 1;
        this.current.add(s);
        for(Edge e:this.map.get(s)){
            if(this.current.contains(e.t)) continue;
            if(e.t.equals(t)) return e.v;
            double temp = this.dfs(e.t,t);
            if(temp!=-1) return temp*e.v;
        }
        return -1;
    }
}