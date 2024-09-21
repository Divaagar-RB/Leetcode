class Solution {
public:
   
    bool isPossible(vector<vector<int>>&grid,int i,int j){
        
         return (i >= 0 && j >= 0 && i < grid.size() && j < grid[0].size() && grid[i][j] == 1);

    }
    void dfs(int i,int j,vector<vector<int>>& grid,int &ans){
        if(grid[i][j]==0||grid[i][j]==2) return;
        grid[i][j]=2;
        ans=ans+1;
        
         if (isPossible(grid, i + 1, j)) {
            dfs(i + 1, j, grid,ans);
        }
        if(isPossible(grid,i-1,j)){
            dfs(i-1,j,grid,ans);
        }
        if(isPossible(grid,i,j+1)){
            dfs(i,j+1,grid,ans);
        }
        if(isPossible(grid,i,j-1)){
            dfs(i,j-1,grid,ans);
        }
     
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int maxi=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    int ans=0;
                    dfs(i,j,grid,ans);
                   
                    maxi=max(ans,maxi);
                   
                    
                }
            }
        }
      return maxi;  
        
        
    }
};