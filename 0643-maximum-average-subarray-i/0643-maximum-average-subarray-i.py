class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxaverage = float("-inf")
        sum = 0
        for i in range(k):
            sum = sum + nums[i]
        maxaverage = sum/k
        j = 0
        for i in range(k,len(nums)):
            sum = sum - nums[j]
            sum = sum + nums[i]
            average = sum/k
            maxaverage = max(average , maxaverage)
            j+=1
        return maxaverage

        