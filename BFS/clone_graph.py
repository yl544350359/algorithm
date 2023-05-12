"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        head=Node(node.val)
        visit={}
        visit[node.val]=head
        queue=[(head, node)]
        while queue:
            clone_cur,cur=queue.pop(0)
            if cur.neighbors:
                for n in cur.neighbors:
                    if not n.val in visit:
                        tmp=Node(n.val)
                        visit[n.val]=tmp
                        queue.append((tmp, n))
                    clone_cur.neighbors.append(visit[n.val])
        return head
