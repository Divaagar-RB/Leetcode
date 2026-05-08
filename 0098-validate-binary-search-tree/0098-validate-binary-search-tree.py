# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        self.ans = True
        def inorder(node):
            if node is  None:
                return
            inorder(node.left)
           

            if self.prev >= node.val:
                self.ans = False
                return
            self.prev = node.val
            
           
            inorder(node.right)
        inorder(root)
        return self.ans
        

      
        