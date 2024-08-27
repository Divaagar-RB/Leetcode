class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j=nums.size()-1;
        for(int i=0;i<nums.size();i++){
            if(i>j) break;
            if(nums[i]==val){
                while(j>i && nums[j]==val) j--;
              if(i<j) { swap(nums[j],nums[i]);
                j--;}
                else {
                    j--;  
                }
            }
          
        }
       return j+1;   
    }
};