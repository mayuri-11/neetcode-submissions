# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            if left < 0:
                left = 0
            
            if right < 0:
                right = 0

            self.maxi = max(self.maxi, root.val + left + right)

            return root.val + max(left, right)
        
        solve(root)
        return self.maxi
        