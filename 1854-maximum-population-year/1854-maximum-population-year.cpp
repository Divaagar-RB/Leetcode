class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int population[101]={0};
        for(const auto log:logs){
            population[log[0]-1950]++;
            population[log[1]-1950]--;
            
        }
        int current =0;
        int maxi=0;
        int maxyear=0;
        for(int i=0;i<101;i++){
            current+=population[i];
            if(current>maxi){
                maxi=current;
                maxyear=1950+i;
            }
        
        }
        return maxyear;
    }
};