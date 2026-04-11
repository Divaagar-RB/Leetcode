class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j=nums.size()-1;
        for(int i=0;i<nums.size();i++){
            if(i>j) break;
            if(nums[i]==val){
                while(nums[j]==val) j--;
                swap(nums[j],nums[i]);
                j--;
            }
          
        }
       return j;   
    }
};