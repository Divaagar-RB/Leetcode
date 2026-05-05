class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        val = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:val+1],inorder[:val])
        root.right = self.buildTree(preorder[val+1:],inorder[val+1:]) 
        return root
