class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> temp(nums1.size(), -1);  // Initialize result with -1
        
        for(int i = 0; i < nums1.size(); i++) {
            bool found = false;
            
            // Find the position of nums1[i] in nums2
            for(int j = 0; j < nums2.size(); j++) {
                if(nums2[j] == nums1[i]) {
                    found = true;
                }
                
                // Once found, look for the next greater element
                if(found && nums2[j] > nums1[i]) {
                    temp[i] = nums2[j];
                    break;
                }
            }
        }
        
        return temp;
    }
};
