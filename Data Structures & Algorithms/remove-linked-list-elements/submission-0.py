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
        curr = dummyNode

        while curr.next != None:
            # if he value is same
            if curr.next.val == val:
                curr.next = curr.next.next
            # else just iterate through the cursor
            else:
                curr = curr.next
        
        return dummyNode.next


