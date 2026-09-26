# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            new_element = Node(insertVal)
            new_element.next = new_element
            return new_element
        
        cursor = head
        while True:
            # Case 1: insertVal lies between cursor and cursor.next
            if cursor.val <= insertVal <= cursor.next.val:
                break
            # Case 2: cursor is the maximum node and cursor.next is the minimum node
            elif cursor.val > cursor.next.val:
                if insertVal >= cursor.val or insertVal <= cursor.next.val:
                    break
            cursor = cursor.next
            # Case 3: looped all the way back to head (e.g. all nodes have the same value)
            if cursor == head:
                break
        
        new_element = Node(insertVal, cursor.next)
        cursor.next = new_element
        return head