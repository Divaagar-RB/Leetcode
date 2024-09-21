class Solution {
public:
    bool isPossible(vector<vector<char>>&grid,int i,int j){
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j]!='1') 
{
            return false;
        }
        return true;
    }
    void dfs(int i,int j,vector<vector<char>>& grid){
        if(grid[i][j]=='0'||grid[i][j]=='X') return;
        grid[i][j]='X';
         if (isPossible(grid, i + 1, j)) {
            dfs(i + 1, j, grid);
        }
        if(isPossible(grid,i-1,j)){
            dfs(i-1,j,grid);
        }
        if(isPossible(grid,i,j+1)){
            dfs(i,j+1,grid);
        }
        if(isPossible(grid,i,j-1)){
            dfs(i,j-1,grid);
        }
        
    }
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]=='1'){
                    dfs(i,j,grid);
                    ans++;
                }
            }
        }
      return ans;  
    }
};