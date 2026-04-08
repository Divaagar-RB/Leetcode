class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
      const   int n=matrix.size();
       const int m= matrix[0].size();
        int row[10]={0};
	int column[10]={0};
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(matrix[i][j]==0){
				row[i]=1;
				column[j]=1;
			}
		}
	}
	for(int i=0;i<n;i++){
                for (int j = 0; j < m; j++) {
					if(row[i]||column[j]){
						matrix[i][j]=0;
					}
                }
        }

        
    }
};