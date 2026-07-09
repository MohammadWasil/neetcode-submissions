# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
               [0 -> 1 -> 2 -> 3]
        prev   cur   next
        None  <-  0   1 -> 2 -> 3]
                prev cur  next

        """

        prev = None
        curr = head

        while curr:
            next_ = curr.next # 1
            curr.next = prev # None <- 0
            prev = curr
            curr = next_
        
        return prev




