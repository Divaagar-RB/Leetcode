# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        def treepath(node,currpath):

            currpath = currpath+str(node.val)+"->"
            if node.left is None and node.right is None:
                temp="->"+str(node.val)

                self.ans.append(currpath[:-2])
                return
            
            if node.left:
               
                treepath(node.left,currpath)
            if node.right:
                treepath(node.right,currpath)
        
        treepath(root,"")
        return self.ans

        