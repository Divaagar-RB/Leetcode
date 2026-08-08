# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = None
        right = None
        if root is None:
            return None
        if root == p or root == q:
            return root
        if root.val > p.val or root.val > q.val:
            left = self.lowestCommonAncestor(root.left,p,q)
        if root.val < p.val or root.val < q.val:
            right = self.lowestCommonAncestor(root.right ,p,q)

        if left and right:
            return root
        return left if left else right
        