# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        array = []

        while curr != None:
            array.append(curr.val)
            curr = curr.next
        
        # [1, 2, 3, 2, 1]
        #  l           r
        # compare l and r, if they are unequal, stop.
        # if they are equal, l+1 and r-1
        # loop until l < r, we dont do l==r
        #l = 0
        #r = len(array) - 1
        
        #while l < r:
        #    if array[l] != array[r]:
        #        return False
        #    l += 1
        #    r -= 1
        
        #return True

        # ==============================#
        # second method:
        # [1,    2, 3, 2, 1]
        # find the middle -> fast and slow pointer technique
        # split, and reverse the second linkedlist
        # iterate thorugh boht of them and check if they are equal or not.

        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # end of the loop, slow gives us the midde of the linkedin list.

        # reverse the second linkedinlist
        #       [  3,   2,   1]
        #    prev slow next 
        curr = slow
        prev = None
        next_ = curr.next

        # None <- 3 -X- 2 -> 1
        #        curr  next

        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        # head node is prev

        # now compare both the linkedlist one by one
        while head != None and prev != None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
