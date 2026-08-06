# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            local_max = float("-inf")
            global_max = float("-inf")
            for i in range(size):
                root = queue.popleft()
                local_max = root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                global_max = max(global_max , local_max)
            result.append(global_max)
        return result
            
                
        