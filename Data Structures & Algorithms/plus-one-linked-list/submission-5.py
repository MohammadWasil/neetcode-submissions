# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        dummyNode = ListNode(-1, head)
        prev = None
        curr = dummyNode #.next
        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        cursor = prev
        oneth_place = True
        while cursor != None:
            if oneth_place and cursor.val != -1:
                new_value = cursor.val + 1
            elif oneth_place and cursor.val == -1:
                new_value = 1
                new_node = ListNode(new_value, None)
                cursor.next = new_node
            else: 
                new_value = cursor.val
            if new_value == 10:
                cursor.val = 0 #new_value % 10
                oneth_place = True
            else:
                cursor.val = new_value
                oneth_place = False
            cursor = cursor.next
        
        curr = prev # from the previous reverse
        prev = None
        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev.next