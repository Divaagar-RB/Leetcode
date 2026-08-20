class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = 0
        for num in nums:
            total+=num
        find = total - x
        temp = 0
        left , right = 0,0
        res = -1
        while right < len(nums):
            temp = temp + nums[right]
            while temp > find and left <= right:
                temp = temp - nums[left]
                left+=1

            if temp == find:
                res = max(res,right-left+1)
            
               
            right+=1
        
        return res if res== -1 else len(nums)-res

        