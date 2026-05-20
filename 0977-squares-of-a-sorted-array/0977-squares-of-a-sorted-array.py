class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k = len (nums)-1
        res = [0] * (k+1);
        while i <= j:
            if abs(nums[i])<abs(nums[j]):
                res[k]=(nums[j]*nums[j])
                j-=1
            else:
                res[k]=(nums[i]*nums[i])
                i+=1
            k-=1
        return res