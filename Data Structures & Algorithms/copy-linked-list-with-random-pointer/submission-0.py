"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {}

        dummy = Node(0, head)
        cur = dummy

        while head:
            if head in oldToNew:
                cur.next = oldToNew[head]
            else:
                cur.next = Node(head.val)
                oldToNew[head] = cur.next

            if head.random in oldToNew:
                cur.next.random = oldToNew[head.random]
            else:
                if head.random:
                    cur.next.random = Node(head.random.val)
                    oldToNew[head.random] = cur.next.random
                else:
                    cur.next.random = None

            cur = cur.next
            head = head.next 

        return dummy.next
