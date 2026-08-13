class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        temp = [0]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                temp[i]=0
            else:
                temp[i]=1
        sum = 0
        res = []
        for i in range(1,k):
            sum = sum + temp[i]
        
        if sum == 0:
            res.append(nums[k-1])
        else:
            res.append(-1)
        
        for i in range(k,len(nums)):
        
            sum = sum + temp[i] - temp[i+1-k]
            if sum == 0:
                res.append(nums[i])
            else:
                res.append(-1)
        return res
