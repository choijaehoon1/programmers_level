import java.util.*;

class Solution {
    
    public int bfs(int node, LinkedList<Integer>[] board, int[] dist){
        dist[node] = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(node);
        
        while(!q.isEmpty()){
            int x = q.poll();
            
            Iterator<Integer> tmp = board[x].listIterator();
            
            while(tmp.hasNext()){
                int i = tmp.next();
                if (dist[i] == -1){
                    dist[i] = dist[x] + 1;
                    q.add(i);
                }   
            }            
        }
        
        int max_value = 0;
        for(int i:dist){
            if(i > max_value){
                max_value = i;
            }
        }
        
        return max_value;

    }
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        LinkedList<Integer>[] board = new LinkedList[n+1];
        
        for(int i=1; i < n+1; i++){
            board[i] = new LinkedList<Integer>();
        }
        
        for(int i=0; i < edge.length; i++){
            int a = edge[i][0];
            int b = edge[i][1];    
            board[a].add(b);
            board[b].add(a);
        }
        
        // for(int i=0; i< board.length;i++){
        //     System.out.println(board[i]);
        // }

        int[] dist = new int[n+1];
        Arrays.fill(dist,-1);
        
        int num = bfs(1,board,dist);
        
        for(int i: dist){
            if(i == num){
                answer += 1;
            }
        }
            
        return answer;
    }
}
