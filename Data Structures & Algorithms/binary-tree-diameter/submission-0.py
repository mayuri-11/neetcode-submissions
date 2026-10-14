# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            dia = left + right
            self.maxi = max(self.maxi, dia)

            return 1 + max(left, right)
        
        solve(root)

        return self.maxi
        