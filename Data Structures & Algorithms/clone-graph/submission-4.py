"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
        m = {} 

        return self.dfs(node, m)



    def dfs(self, node, m):
        if not node:
            return None
    
        if node in m:
            return m[node]
        
        res = Node(node.val)
        m[node] = res
        for nei in node.neighbors:
            res.neighbors.append(self.dfs(nei, m))
        
        return res
            
            
        
        


