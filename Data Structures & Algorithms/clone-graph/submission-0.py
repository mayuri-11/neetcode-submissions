"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapp = {}

        def dfs(old):
            if old in mapp:
                return mapp[old]
            
            copy = Node(old.val)
            mapp[old] = copy
            

            for nei in old.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None

        