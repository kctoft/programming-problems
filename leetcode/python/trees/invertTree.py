#  Invert Binary Tree
# Link:https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
     # Base case: check if root is null
    if not root:
        return None

    # swap children DFS
    temp = root.left
    root.left = root.right
    root.right = temp

    # recursive call to both subtrees
    self.invertTree(root.left)
    self.invertTree(root.right)
    # return the root
    return root
