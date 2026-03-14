class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        maxsum = float('-inf')
        minsum = float('inf')
        sum = 0
        for num in nums:
            sum = sum + num
          
            maxsum = max(maxsum,sum)
            if sum < 0:
                sum = 0
        sum = 0
        for num in nums:
            sum = sum + num
           
            minsum = min(minsum,sum)
            if sum > 0:
                sum = 0
        print(maxsum)
        print(minsum)                
        return max(abs(minsum),maxsum)
        