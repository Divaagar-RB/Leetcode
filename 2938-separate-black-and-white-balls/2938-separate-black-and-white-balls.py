class Solution:
    def minimumSteps(self, s: str) -> int:

        nums = list(s)
        i = 0
        j = 0
        count = 0
        while i < len(nums):
            if nums[i]=="0":
                nums[i],nums[j]=nums[j],nums[i]
                count = count + (i-j)
                j+=1
                
            i+=1
        return count