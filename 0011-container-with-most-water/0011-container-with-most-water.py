class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxwater = float('-inf')
        while start < end:
            length = end - start
            print(length)
            area = length * min(height[start] , height[end])
            print(area)
            maxwater = max(area,maxwater)
            if height[start] <= height[end]:
                start +=1
            else:
                end-=1

        return maxwater


        