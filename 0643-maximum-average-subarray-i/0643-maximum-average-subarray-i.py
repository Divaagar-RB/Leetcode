class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxaverage=float('-inf')
        total_sum = 0
        for i in range(k):
            total_sum = total_sum +  nums[i]
        maxaverage = total_sum /k
        
        for i in range(k,len(nums)):
            total_sum = total_sum + nums[i] - nums[i-k]
            print(nums[i-k])
            average = total_sum/k
            maxaverage = max(average,maxaverage)
        return maxaverage
        