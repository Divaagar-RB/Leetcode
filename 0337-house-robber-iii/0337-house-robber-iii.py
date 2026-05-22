# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.amount = 0
        def postorder(node):
            if node is None:
                return [0,0]
            left = postorder(node.left)
            right = postorder(node.right)
            withroot = left[1]+right[1]+node.val
            withoutroot = max(left) + max(right)
            return [withroot, withoutroot]
        val = postorder(root)
        return max(val[0],val[1])