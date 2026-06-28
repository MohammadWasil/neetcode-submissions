# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # search for the value in the balanced BST
        # Either in the left sub tree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Either in the right sub tree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Or none of the above, means we fund the value in the "root"
        else:
            # If the left child is absent, return the rght one to be deleted.
            if not root.left:
                return root.right
            # If the right child is absent, return the rght one to be deleted.
            elif not root.right:
                return root.left
            # But if both of the children are present in the root, 
            # then we need to replace the root (the target) with the min value of the right subtree
            # or maxiumum value of the left subtree
            #else:
            # To find the minimum value from the "right" sub tree
            
            # take the right sub tree
            curr = root.right 
            # find the minimum value
            minimum_value = self.minimum_node_value(curr) 
            # reaplce the min value with the root node
            root.val = minimum_value.val
            # delete the mini valu from the right sub tree
            root.right = self.deleteNode(root.right, minimum_value.val)
        
        return root
    
    def minimum_node_value(self, curr):
        
        while curr and curr.left: # and then take the left most element
            curr = curr.left 
        return curr # loop until we reach the end of the tree -> left node





