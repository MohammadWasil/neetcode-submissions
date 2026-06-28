# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
                1
            2       3
        4     5    6
                  [1, 3, 5]
        
        FIFO_Q = [1-1, 2-2, 3-3, 4-4, 5-5]
        res = [1, 3, 4]
        """
        res = []
        queue = deque()
        if not root:
            return []
        queue.append(root) # [1]
        

        # loop thorugh until the queue is not empty
        while queue: # [1] -> [2, 3]
            rightside = None
            # iterate all the avlues in the queue
            for i in range(len(queue)):
                curr = queue.popleft() # [2-2, 3-3]
                if curr.left:
                    queue.append(curr.left) # [2] -> [3, 4] -> [4, 5, 6]
                if curr.right:
                    queue.append(curr.right) # [2, 3] -> [3, 4, 5] -> [4, 5, 6]
                rightside = curr
            if rightside:
                res.append(rightside.val) # [1] -> [1, 3,] -> [1, 3, 6]
        
        return res
                








        
        