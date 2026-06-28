# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

                1   ->[1]
            2       3  -> [2, 3]
        4   5       6   7 -> [4, 5, 6, 7]

        arr = adding here -> [1-1, 2-2, 3-3, 4-4, 5-5, 6-6, 7-7] <- removing from here = Queue

        res = [[1], [2,3], [4, 5, 6, 7]]

        """

        if not root:
            return []
        
        res = []
        queue = deque()
        # Root can be added to an queue
        queue.append(root)

        # Add the node val in the resultant list
        res.append([root.val])        

        level = 0
        # loop thorugh the queue
        while queue: #[2-2, 3]
            
            temp_inner_list = []    
            for q in range(len(queue)):
                # remove the current node from queue
                curr = queue.popleft()
                if curr.left:
                    # Add the new node into the queue
                    queue.append(curr.left)
                    # Add the node vale in resultant list
                    temp_inner_list.append(curr.left.val) #[4]
                if curr.right:
                    # Add the new node into the queue
                    queue.append(curr.right)
                    # Add the node vale in resultant list
                    temp_inner_list.append(curr.right.val) # [4, 5]
            if temp_inner_list:
                res.append(temp_inner_list)
            # end the loop when queue is empty

        return res



        