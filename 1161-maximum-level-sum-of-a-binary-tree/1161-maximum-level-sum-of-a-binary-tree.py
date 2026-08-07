# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxSum = float("-inf")
        maxSumLevel = None
        currentLevel = 0
        while queue:
            size = len(queue)
            levelSum = 0
            currentLevel+=1
            for i in range(size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                levelSum = levelSum + root.val
            if levelSum > maxSum:
                maxSum = levelSum
                maxSumLevel = currentLevel

        return maxSumLevel

                    
            
        