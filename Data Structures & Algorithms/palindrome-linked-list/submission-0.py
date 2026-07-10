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
        l = 0
        r = len(array) - 1
        
        while l < r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1
        
        return True