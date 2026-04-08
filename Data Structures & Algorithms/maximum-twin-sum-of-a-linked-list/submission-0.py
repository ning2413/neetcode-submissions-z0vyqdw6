# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk = []
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        while s:
            stk.append(s.val)
            s = s.next

        maxVal = 0
        while stk:
            t1 = head.val
            t2 = stk.pop()
            maxVal = max(maxVal, t1 + t2)
            head = head.next
        return maxVal


