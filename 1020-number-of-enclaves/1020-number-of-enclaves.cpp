class Solution {
public:
     void dfs(int i, int j, vector<vector<int>>& grid) {
        // Return if out of bounds or if the cell is water (0) or already visited (2)
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] != 1)
            return;
        
        // Mark the current land cell as visited
        grid[i][j] = 2;
        
        // Continue DFS in all 4 directions
        dfs(i + 1, j, grid);
        dfs(i - 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i, j - 1, grid);
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans=0;
        for(int i=0;i<n;i++){
            if(grid[i][0]==1){
                dfs(i,0,grid);
                }
            if(grid[i][m-1]==1){
                dfs(i,m-1,grid);
            }
        }
        for(int j=0;j<m;j++){
            if(grid[0][j]==1){
                dfs(0,j,grid);
                }
            if(grid[n-1][j]==1){
                dfs(n-1,j,grid);
               }
        }
        for(int i=1;i<n-1;i++){
            for(int j=1;j<m-1;j++){
                if(grid[i][j]==1){
                    ans++;
                }
            }
        }
        return ans;
    }
    
};