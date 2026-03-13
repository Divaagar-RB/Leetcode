class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        evenbest = 0
        odd = 0
        temp = nums[:]
        for i in range(1,len(nums),2):
            if i+1<len(nums):
                if nums[i+1] >= nums[i]:
                    
                    evenbest = evenbest +( nums[i+1]-nums[i])+1
                    nums[i+1] = nums[i]-1
                if nums[i-1] >= nums[i]:
                    evenbest = evenbest +( nums[i-1]-nums[i])+1
                    nums[i-1] = nums[i]-1
            else:
                if nums[i-1] >= nums[i]:
                    evenbest = evenbest +( nums[i-1]-nums[i])+1
                    nums[i-1] = nums[i]-1
        nums = temp[:]  
        for i in range(1,len(nums),2):
            if i+1<len(nums):
                if nums[i+1] <= nums[i]:
                    odd = odd +( nums[i]-nums[i+1])+1
                    nums[i] = nums[i+1]-1
                    
                if nums[i-1] <= nums[i]:
                    odd = odd +(nums[i]-nums[i-1])+1
                    nums[i] = nums[i-1]-1
            else:
               if nums[i-1] <= nums[i]:
                    odd = odd +( nums[i]-nums[i-1])+1
                    nums[i] = nums[i-1]-1
                    
            
        return min(odd,evenbest)