# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        1. Reverse the node
        2. prev now points to the head of the reversed node.
        3. Add the one to the cursor at the head node.
        4. Depending on the output, if the addition is 10, update the cursor node val as only 0
        5. And for the next iteration, add the remining 1 to the cursor val.
        6. Special case: When we have the last dummy node with carry of 1, add a new dummy node with value 1.
        7. Reverse the linkedlist again. Use the prev counter, pointing to the head of the current linkedlist.
        """

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