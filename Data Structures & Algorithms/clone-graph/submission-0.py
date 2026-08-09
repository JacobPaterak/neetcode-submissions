"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
        
            if not node:
                return
            if node in seen:
                return seen[node]
            
            new_node = Node(val = node.val)
            seen[node] = new_node
            for child in node.neighbors:
                new_node.neighbors.append(dfs(child))
        
            return new_node
        return dfs(node)