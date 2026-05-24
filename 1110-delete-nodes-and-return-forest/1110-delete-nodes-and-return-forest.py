# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_d = set(to_delete)
        self.ans = []
        
        def postorder(node , prev ,side):
            if node is None:
                return  None
            left = postorder(node.left , node , "left")
            right = postorder(node.right , node , "right")
            

            
            if node.val in to_d:
               
                if node.left  and node.right :
                    self.ans.append(node.left)
                    self.ans.append(node.right)
                   
            
                elif node.left:
                    self.ans.append(node.left)
                    
                elif node.right:
                    self.ans.append(node.right)
                    
                
                node.left = None
                node.right = None
                if prev:
                    
                    if side == "left":
                        prev.left = None
                       
                    else:
                        prev.right = None
                       
                    
                
            return 1

       
        postorder(root,None,"root")
        if root.val not in to_d:
            self.ans.append(root)
        
             
        return self.ans

                    