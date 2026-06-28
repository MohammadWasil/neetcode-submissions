class MinHeap:
    
    def __init__(self):
        self.heap=[0]

    def push(self, val: int) -> None:
        """
        val = 70
                                                val
        [0,  10, 30, 20, 50, 80, 70, 40, 90, 60, 70]

                            10
               30                       20
            50    80              70          40
        90 60    70 Null      Null Null    Null Null
                val

        # Find the parents of the val -> index // 2 ==> heap[5] = 80

        # compare the parent and the child
        # i child < parent: then swap, else fine

        # update the index to index//2
        # compare the parent and the child again
        """
        self.heap.append(val)
        index = len(self.heap) - 1

        # Percolate upwards
        while index // 2 > 0 and self.heap[index] < self.heap[index//2]:
            # swap
            temp = self.heap[index//2] 
            self.heap[index//2] = self.heap[index]
            self.heap[index] = temp 

            index = index // 2 # udate the index to where the parent was before

    def pop(self) -> int:
        """
        [0,  10, 30, 20, 50, 80, 70, 40, 90, 60]
        # percolate it down
        """

        if len(self.heap) <= 1 :
            return -1
        if len(self.heap) == 2: # [0, 10]
            return self.heap.pop()
            
        # the result value to return
        smallest_element = self.heap[1]

        # remove the last elemtn from the list, and add it to the first index
        self.heap[1] = self.heap.pop()

        i = 1
        self.percolate_down(i)

        return smallest_element

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def percolate_down(self, i: int) -> None:
        # atleast left child is present
        while 2 * i < len(self.heap):
            # if the right child exists, AND right child is smaller than the left child, 
            # AND right child is smaller than the parent
            if 2*i+1 < len(self.heap) and self.heap[(2*i)+1] < self.heap[2*i] and self.heap[(2*i)+1] < self.heap[i]:
                # swap the right child with the parent
                temp = self.heap[i]
                self.heap[i] = self.heap[(2*i)+1]
                self.heap[(2*i)+1] = temp
                i = 2*i+1 # so that we can percolate further down from this right child

            # means left child is greater than the right, so we now cpmpare left child and the parent
            # compares the left child is bigger than the parent 
            elif self.heap[2*i] < self.heap[i]:
                # perform swap of left with parent
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = temp
                i = 2*i # so that we can percolate further down from this left child
            else:
                break

    def heapify(self, nums: List[int]) -> None:
        """
        [60, 50, 80, 40, 30, 10, 70, 20, 90]
        [0,  50, 80, 40, 30, 10, 70, 20, 90, 60] 
        L child = 2*i
        R child = (2*i)+1
        Parent = i // 2
        curr = (len(nums)-1 ) // 2
        """
        if len(nums) <= 1:
            return

        # take the first element and add it to the end.
        nums.append(nums[0])

        self.heap = nums

        # the cursor should always be on the last node with atleast one child
        curr = (len(self.heap) - 1) // 2

        # [0, 50, 80, 40, 30, 10, 70, 20, 90, 60]
        #                 curr
        #             curr
        """
                            50
               80                       40
            30     10              70          20
        90 60    Null Null      Null Null    Null Null
        """
        while curr > 0:
            i = curr # create a copy
            # the percolation down  algorithm
            
            self.percolate_down(i)
            
            curr -= 1











        
        