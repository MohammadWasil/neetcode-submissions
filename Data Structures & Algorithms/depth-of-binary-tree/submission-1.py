# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS -> traverse every level one by one, and coutn the number of levels.
                    1   <-
                2       3
            nu  nu      4   nu
        queue = [1]
        while
        iterate through all the values in the queue
        take 1, and find its left and right subtree, if found, add them to the queue.
        remove 1, inceament the depth fo the tree.
        """
        queue = deque()
        if root:
            queue.append(root)
        depth = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            depth += 1
        return depth