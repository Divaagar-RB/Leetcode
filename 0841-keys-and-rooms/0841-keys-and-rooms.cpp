class Solution {
public:
    void bfs(int node, vector<vector<int>>& isConnected, vector<bool>& visit) {
    queue<int> q;
    q.push(node);
    visit[node] = true;

    while (!q.empty()) {
        int currentNode = q.front();
        q.pop();

        
        for (int i = 0; i < isConnected[currentNode].size(); i++) {
            int nextRoom = isConnected[currentNode][i];
            if (!visit[nextRoom]) {
                q.push(nextRoom);
                visit[nextRoom] = true;
            }
        }
    }
}

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        
         vector<bool> visited(rooms.size());
          bfs(0, rooms, visited);
        for(int i=0;i<visited.size();i++){
            if(visited[i]==false){
                return false;
            }
        }
      return true;  
    }
};