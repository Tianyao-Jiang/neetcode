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

        def dfs(node):
            if not node:
                return node

            if node in m:
                return m[node]

            new_node = Node(node.val)
            m[node] = new_node

            new_neighbors = []
            for nei in node.neighbors:
                new_neighbors.append(dfs(nei)) 
                new_node.neighbors = new_neighbors
            
            return new_node

        return dfs(node)