class LinkedNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Define the (dummy) head and the tail node.
        self.head = LinkedNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next # the reason for the next node, is that
        # since the head node is the dummy node, we go with the node right next to it.
        # the dummy noe was added by us.
        i = 0
        while curr:
            if i == index:
                return curr.val # if we foudn the current node we want to find, return their val.
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        # Create a new node, called it new_node
        new_node = LinkedNode(val)
        # point the pointer of the new_node to the same node as it was for the Head Node.
        new_node.next = self.head.next
        # Now point the pointer of the head node to the new node that you ceated.
        # this makes sure that the old pointer of the head, which was pointing towards the other one
        # (now new node point to that), now points to the new node.
        self.head.next = new_node
        # In case there were no nodes, and the linked list was empty before insertion
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # crate a new node with the value
        # point the next pointer of the tail node to the newly created node.
        self.tail.next = LinkedNode(val)
        # Then update your tail to the newly added node, which is being pointed
        # by, none other than, self.tail.next
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0 # for traversing
        curr = self.head # for pointing to the current node, strt from the head

        # need to stop one node before the index node (the Node which we are trying to find)
        # and also making sure the next node do exists in the LinkedList
        while i < index and curr.next:
            i += 1 # move the index
            curr = curr.next # move the current pointer

        # compare 
        if curr and curr.next: # if the both of the node are not null
            # what if the next node if the curr is a Tail?
            if curr.next == self.tail:
                self.tail = curr # then make sure to make the curr node the Tail of the LinkedList
            # remove the next node (after curr)
            # by assigning the next of the curr with next.next (one node after the one which 
            # we are supposed to skip)
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next # not including the head / dummy node
        res = []

        while curr:
            res.append(curr.val)    # get the value of the current node
            curr = curr.next        # ove the curr to the next node.
        return res
        
