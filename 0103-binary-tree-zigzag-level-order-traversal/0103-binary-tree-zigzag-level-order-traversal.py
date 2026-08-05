# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        j  = 0 
        while queue:
            current =[]
            size = len(queue)
           
            for i in range(size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
             

                current.append(root.val)
          
            res.append(current[::-1]) if j%2==1 else res.append(current[:])
            
           
            j+=1
        return res
    
        