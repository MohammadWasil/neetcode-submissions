# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # the first element will always eb the root node
        root_val = preorder[0]

        # create the node
        root = TreeNode(root_val)

        # find the root value in the order array
        root_index = inorder.index(root_val)

        num_left_subtree = root_index
        num_right_subtree = len(inorder) - (root_index + 1)

        # this exlcudes num_left_subtree index
        #left_subtree = preorder[1:num_left_subtree+1]
        #inorder_left = inorder[:root_index]
        #root.left = self.buildTree(left_subtree, inorder_left)

        # this includes num_right_subtree index
        #right_subtree = preorder[num_right_subtree:]
        #inorder_right = inorder[root_index+1:]
        #root.right = self.buildTree(right_subtree, inorder_right)

        root.left = self.buildTree(preorder[1 : root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1 :], inorder[root_index + 1 :])

        return root
