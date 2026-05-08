# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        self.prev = float('inf')
        self.minimum = float('inf')
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.diff = abs(self.prev-node.val)
           
            self.minimum = min(self.diff,self.minimum)
            self.prev=node.val
          
            

            inorder(node.right)
        inorder(root)
        return self.minimum



        