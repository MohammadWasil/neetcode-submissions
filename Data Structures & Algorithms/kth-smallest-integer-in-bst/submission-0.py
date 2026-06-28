# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            2
        1       3

        Perform DFS - inorder traversal
        and populate list

        list = [] O(n)  where n is the number of elements in the left most sub tree
        populate the list, and at the end, select the kth element (1st index)
        left_values = [2, 1]
                       0+1 1+1
        """
        
        traverse_list = []
        root, traverse_list = self.traversal(root, traverse_list)

        # traverse list would already be sorted
        return traverse_list[k-1].val

    def traversal(self, root, traverse_list):
        if not root:
            return None, traverse_list
        
        root.left, traverse_list = self.traversal(root.left, traverse_list)
        traverse_list.append(root)
        root.right, traverse_list = self.traversal(root.right, traverse_list)

        return root, traverse_list
