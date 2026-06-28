# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        input_list = []
        current = head
        while current:
            input_list.append(current.val)
            current = current.next

        # [0, 1, 2, 3, 4, 5, 6]
        new_list = []
        input_len = len(input_list)

        for i in range((input_len//2)+1):
            new_list.append(input_list[i])
            last_index = input_len - i - 1
            if i != last_index:
                new_list.append(input_list[last_index])

        index = 0
        while head and index < input_len:    
            head.val = new_list[index]
            head = head.next
            index += 1


