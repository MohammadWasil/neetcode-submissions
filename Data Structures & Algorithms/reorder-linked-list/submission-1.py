# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # this is a brute force technique
        # time and space complexity is O(n)
        #input_list = []
        #current = head
        #while current:
        #    input_list.append(current.val)
        #    current = current.next

        # [0, 1, 2, 3, 4, 5, 6]
        #new_list = []
        #input_len = len(input_list)

        #for i in range((input_len//2)+1):
        #    new_list.append(input_list[i])
        #    last_index = input_len - i - 1
        #    if i != last_index:
        #        new_list.append(input_list[last_index])

        #index = 0
        #while head and index < input_len:    
        #    head.val = new_list[index]
        #    head = head.next
        #    index += 1

        """
        curr = head

        # get the last element form inkedin list
        #while head:
        #    tail = curr.next
        tail = self.get_tail(curr)

        while head and head.next:
            tail.next = head.next
            head.next = tail
            
            # somehow need ot pdate the tail
            temp_curr = head
            tail = self.get_tail(temp_curr)

            # updte the curr as well
            head = head.next.next

        def get_tail(self, header):
            # get the last element form inkedin list
            while header:
                tail = header.next
            return tail
        """

        # fine the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # [0, 1, 2, 3, 4, 5, 6]
        #           s        f

        # reverse from the middle - only the second part
        curr = slow.next
        # [0, 1, 2, 3, 4, 5, 6]
        #           s  c     f
        # NULL [4, 5, 6]
        # prev, c, n
        #      prev,c, n
        #         prev,c, n
        #            prev,c, n -> c is null
        # prev = 6, c = null, n = null
        prev = None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        slow.next = None # terminate the first list (head1) properly, break the conenctions.

        # merge the two linked list together
        head1 = head
        head2 = prev
        # head1: [0, 1, 2, 3, 4, 5, 6]
        #         H1-H1
        # head2: [6, 5, 4]
        #         H2-H2
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            # creating connections with pointers
            head1.next = head2
            head2.next = next1

            # update the heads to the next values in the LL
            head1 = next1
            head2 = next2





