# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        curr = head
        prev = curr
        while curr is not None:
            m_count, n_count = m, n
            
            while curr is not None and m_count != 0:
                prev = curr
                curr = curr.next
                m_count -= 1
            
            while curr is not None and n_count != 0:
                curr = curr.next
                n_count -= 1
            
            prev.next = curr

        return head
