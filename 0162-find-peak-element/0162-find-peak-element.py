class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
            
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low + high )//2
            val = nums[mid]
            if mid+1 <= len(nums) and mid-1 >= 0:
                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    return mid-1
                if nums[mid] < nums[mid+1]:
                    low = mid
                else:
                    high = mid
           
        return mid-1