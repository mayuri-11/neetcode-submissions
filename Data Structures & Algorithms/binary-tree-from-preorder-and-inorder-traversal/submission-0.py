# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        
        self.pre = 0
        def solve(l,r):
            if l > r:
                return None
            
            node = TreeNode(preorder[self.pre])
            self.pre += 1

            inidx = mapp[node.val]

            node.left = solve(l,inidx - 1)
            node.right = solve(inidx + 1, r)

            return node
        
        return solve(0,len(preorder) - 1)

        
        