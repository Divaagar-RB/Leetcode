class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return low   #also can return high +1
 #At the end of the loop:
# low points to the correct insertion index.
# high points to the index just before it.
# Therefore, low == high + 1.


        
        