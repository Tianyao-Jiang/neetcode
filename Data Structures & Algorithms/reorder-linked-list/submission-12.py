# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None

        secondHead = self.reverse(temp)

        cur = head
        while secondHead:
            temp = cur.next
            cur.next = secondHead
            temp2 = secondHead.next
            secondHead.next = temp
            cur = temp
            secondHead = temp2

        
    def reverse(self, h):
        prev = None
        while h:
            temp = h.next
            h.next = prev
            prev = h
            h = temp
        return prev
        
