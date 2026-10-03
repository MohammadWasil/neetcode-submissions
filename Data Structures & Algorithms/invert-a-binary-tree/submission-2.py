# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
                    1
                2       3
            4   5       6   7

        take the root, and l and r child, and replace them inpace.
        And use DFS to iteretae.
        root 1, 
        left 2
        right 3
            1                   1
        2   3       < ->    3       2

        now, 
        left 3
        right 2

        run inverttree again on 3 and 2 separately.

            root 3
            left 6
            right 7
                3               3
            6   7       <->   7   6

                Now take the left tree again
                root 7
                left null, right null
            
                Now take the right tree
                root 6
                left null, right null

                return
            
            root 2
            left 4
            right 5
                2               2
            4   5       <->     5   4

                Now take the left tree again
                root 5
                left null, right null
            
                Now take the right tree
                root 4
                left null, right null

                return
        
        return the root.

                1
            3       2
        7   6       5   4
        """
        """if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        """


        """
        BFS approach:
                    1
                2       3
            4   5       6   7


        Q = [1]
        loop 0:
        remove 1 from Q, Q = []
        root 1, l=2, r=3 -> replace them => l=3, r=2

                     1
                3       2
            6   7       4   5
        Q = [3, 2]
        
        loop 1:
        remove 3 from Q, Q=[2]
        root 3, l=6, r=7 , replace=> l=7, r=6
                     1
                3       2
            7   6       4   5
        q = [2, 7, 6]

        loop 2:
        remove 2 frm Q, Q=[7, 6]
        root =2, l=4, r=5, replace them => l=5, r=4
                     1
                3       2
            6   7       5   4
        Q=[7, 6, 5, 4]

        ...and d the same for 7, 6, 5, 4...
        """
        if not root:
            return None
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root