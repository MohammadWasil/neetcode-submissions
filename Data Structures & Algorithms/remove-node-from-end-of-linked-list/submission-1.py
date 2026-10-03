# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        length = 4
        n=2 from the end
        1 -> 2 -> 3 -> 4
                  n
        0    1    2    3 <- and then length - n = 4 - 2 = 2
        x    x    2    x <- index=2 to be removed form the begining.

        Now iterate the linklist, and skip the node with index=2

            1 -> 2 -> 3 -> 4
            c
           i=0
           compare the next index i+1 with index=2, if the same, skip the next node.
           else c.next and move to the next index, i
           i+1 = 0+1 = 1 <-> index = 2 -> false -> c.next, 

                c
               i=1
               i+1 = 1+1=2 <-> index = 2 < True, c.next.next and stop the program
        """
        """
        # first calculate the length of the linklist
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next

        # get the index we need to remove from the end, and convert it to index from the begining.
        index = length - n

        if index == 0:
            return head.next

        cursor = head
        for i in range(length - 1):
            if i+1 == index:
                # skip the next node
                cursor.next = cursor.next.next
                break
            cursor = cursor.next

        return head
        """

        """
        Second way: Two pointer solution

        1 -> 2 -> 3 -> 4

        add dummynode, and l and r pointer

        0 -> 1 -> 2 -> 3 -> 4
        l    r

        Idea: move the r to the index to be removed, and aferwards, move both l and r at the same time.
        when r is pointing to null, l would point to the node which needs to be removed.

            0 -> 1 -> 2 -> 3 -> 4
            l    r
            l         r
                           r
            
            Now move both l and r
            0 -> 1 -> 2 -> 3 -> 4
                 l              r
                      l             r 
                      next loop, the r is pointing tot he null, meaning l is ptining to the index to be removed.
        """

        dummyNode = ListNode(0, head)
        l = dummyNode
        r = head

        while n > 0:
            r = r.next
            n -= 1
        
        while r != None:
            l = l.next
            r = r.next
        
        # now r is pointing to the none, and l is pointing to the node that we need to remove.
        # which can be skipped
        l.next = l.next.next

        return dummyNode.next