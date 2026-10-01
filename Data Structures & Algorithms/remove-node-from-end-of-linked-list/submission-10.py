# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        cur = dummy
        end = head

        while n > 0 and end:
            end = end.next
            n -= 1

        while end:
            cur = cur.next
            end = end.next
        
        temp = cur.next
        cur.next = cur.next.next
        temp.next = None

        return dummy.next

