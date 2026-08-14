class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = set()
        if k > len(nums)-1:
            k =(len(nums)-1)%k
            print(k)
        for i in range(k+1):
            if nums[i] in hash_table:
                
                return True
            hash_table.add(nums[i])
        print(hash_table)
        for i in range(k+1,len(nums)):
            # print(i)
            # print(hash_table)
            # print(nums[i-k-1])
            hash_table.remove(nums[i-k-1])
            # print(hash_table)
            
            if nums[i] in hash_table:
                return True
            hash_table.add(nums[i])

        return False
    