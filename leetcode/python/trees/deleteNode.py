# [Delete Node in a BST]
# link: (https://leetcode.com/problems/delete-node-in-a-bst/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def deleteNode(self, root, key):
  # use recursion, TC: O(n)
  # Base case: If the root is None, return None
  if not root:
      return None

  # If the key to be deleted is less than the root's key,
  # then the function is recursively called with the left subtree
  if key < root.val:
      root.left = self.deleteNode(root.left, key)
  # If the key to be deleted is greater than the root's key,
  # then the function is recursively called with the right subtree
  elif key > root.val:
      root.right = self.deleteNode(root.right, key)
  else:
      # Case 1: If the root has no children or only one child, then the root is replaced with its child
      if not root.left:
          return root.right
      elif not root.right:
          return root.left
      # Case 2: If the root has two children, then the in-order successor of the root is found
      else:
          # Find the miimum from the right subtree
          cur = root.right
          while cur.left:
              cur = cur.left
          # The value of the in-order successor is copied to the root
          root.val = cur.val
          # The in-order successor is then deleted from the right subtree of the root
          root.right = self.deleteNode(root.right, cur.val)

  return root
