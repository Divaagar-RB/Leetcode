class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        larger = []
        smaller = []
        equal =  []
        for i in nums:
            if i > pivot:
                larger.append(i)
            elif i == pivot:
                equal.append(i)

            else:
                smaller.append(i)
        print(smaller)
        print(larger)
        return smaller[:]+equal[:]+larger[:]
        