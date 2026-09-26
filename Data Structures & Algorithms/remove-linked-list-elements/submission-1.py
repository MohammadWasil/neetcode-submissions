# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 2, 1, 4, 1, 2, 3
        # create a dummy node, with a head of the head
        # dummy   ->   2   ->   1   ->   4   ->   1   ->   2   ->   3
        # curr

        dummyNode = ListNode(-1, head)
        cursor = dummyNode

        while cursor.next != None:
            if cursor.next.val == val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        
        return dummyNode.next
