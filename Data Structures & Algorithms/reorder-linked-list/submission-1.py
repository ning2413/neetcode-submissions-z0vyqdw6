# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        prev = None
        s.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1 = head
        l2 = prev

        while l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2
            l2.next = n1

            l1 = n1
            l2 = n2