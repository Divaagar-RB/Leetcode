# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        temp = []
        while queue:
            size = len(queue)
            current = []
            for i in range(size):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                current.append(top.val)
            temp.append(current)
        res = []
        for t in temp:
            res.append(t[-1])

        return res

        