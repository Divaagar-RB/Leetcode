class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        count = 0
        maxi = 0
        while j <len(nums):
            if nums[j]== 1:
            
                j+=1
            elif k > 0:
            
                k-=1
                j+=1
                
            else:
                maxi = max(maxi,j-i)

                while nums[i]!=0:
                    i+=1
                    count -=1
                i+=1
                k+=1

                
            
        
        maxi = max(maxi,j-i)
        return maxi
            