class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 999999999999
        for i in range(len(nums)):
            j= i+1
            k = len(nums)-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                
                diff_1 = abs(closest-target)
               
                diff_2 = abs(target-total)
                
                if diff_1 > diff_2:
                    closest=total


                if total == target:
                    j+=1
                    k-=1
                elif total > target:
                    k-=1
                else:
                    j+=1

        return closest



        #error due to print statement