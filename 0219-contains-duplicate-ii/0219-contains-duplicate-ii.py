class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #optimised version
        hash_table = set()
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return True
            hash_table.add(nums[i])
            if i >= k:
                hash_table.remove(nums[i-k])
        return False