"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """cursor = head
        dummyNode = Node(0, -1, -1)

        new_ll = dummyNode
        while cursor != None:
            node = Node(cursor.val, -1, -1)
            dummyNode.next = node
            #dummyNode.next.random = cursor.random
            cursor = cursor.next
            dummyNode = dummyNode.next
        return new_ll"""
        if head is None:    
            return None

        l1 = head
        while l1 is not None:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next

        newHead = head.next

        l1 = head
        while l1 is not None:
            if l1.random is not None:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        l1 = head
        while l1 is not None:
            l2 = l1.next
            l1.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
        