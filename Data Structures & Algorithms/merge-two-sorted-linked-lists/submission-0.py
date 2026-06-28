# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # increament the counter of list1
            else:
                tail.next = list2
                list2 = list2.next # increament the counter of list2
            tail  = tail.next # increament the counter of tail
            
        # Even after the loop,there are some elements left in the list1, 
        # add all of them in the tail (since they are already sorted) 
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummyNode.next
        
        