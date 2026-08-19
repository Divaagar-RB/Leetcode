class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 1
        left , right = 0 , 0
        res , temp = 0 , 0
        while right < len(nums):
            if nums[right]==0:
                if count > 0:
                    count-=1
                else:
                    while nums[left]!=0 and left < right:
                        left+=1
                    left+=1
                    
            res = max(res,right-left)
            right+=1
        return res