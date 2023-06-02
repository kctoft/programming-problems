# [Search in a Binary Search Tree]
# link: https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(log n)
def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    # Given the root of a BST and `val`, find the node whch equals val
    # iterate if root is non-null, searching all decendants
    while root != None and root.val != val:
        #  descend to the right if it's greater
        if root.val < val:
            root = root.right
        # descend to the left if val is less than the current node's value
        else:
            root = root.left
    return root
