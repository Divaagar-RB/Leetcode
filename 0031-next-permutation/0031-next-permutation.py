class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        small_index= -1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                small_index = i-1
                break

        if small_index!=-1:
            for i in range(len(nums)-1,small_index,-1):
                if nums[small_index]<nums[i]:
                    nums[small_index],nums[i]=nums[i],nums[small_index]
                    break

        i = small_index+1
        j = len(nums)-1
        while i < j :
             nums[i],nums[j]= nums[j],nums[i]
             i+=1
             j-=1