class Solution {
    public int minTrioDegree(int N, int[][] edges) {
        boolean[][] connected = new boolean[N][N];
        int[] deg = new int[N];
        
        for(int i = 0 ; i < edges.length ; ++i){
            int u = edges[i][0] - 1;
            int v = edges[i][1] - 1;
            connected[u][v] = true;
            connected[v][u] = true;
            deg[u]++;
            deg[v]++;
        }
        
        int total = 100000000;
        for(int i=0 ; i<N ; ++i){
            for(int j = i+1 ; j < N ; ++j){
                if(connected[i][j]){
                    for(int k = j+1 ; k < N ; ++k){
                        if(connected[j][k] && connected[i][k]){
                            total = Math.min(total, deg[i] + deg[j] + deg[k] - 6);
                        }
                    }
                }
            }
        }
        
        if(total == 100000000){
            return -1;
        }
        
        return total;
       
    }
}