class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        
        total =(n*(n-1))//2
        got = 0
        for num in nums:
            got+=num
        return total - got
        