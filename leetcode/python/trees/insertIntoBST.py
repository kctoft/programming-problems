# Insert into a Binary Search Tree
# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/


# recursive solution
def insertIntoBST(self, root, val):
  """
  :type root: TreeNode
  :type val: int
  :rtype: TreeNode
  """
  # base case: if null, insert at root
  if not root:
      return TreeNode(val)

  # check if val is bigger than root
  if val > root.val:
      root.right = self.insertIntoBST(root.right, val)
  # otherwise val is smaller
  elif val < root.val:
      root.left = self.insertIntoBST(root.left, val)
  # return the new BST via root
  return root


# #iterative
# def insertIntoBST(self, root, val):
#   """
#   :type root: TreeNode
#   :type val: int
#   :rtype: TreeNode
#   """
#   # base case: if null, insert at root
#   if not root:
#     return TreeNode(val)
#   cur = root
#   while cur:
#     if val < cur.val:
#       if not cur.left:
#         cur.left = TreeNode(val)
#         return root
#       cur = cur.left
#     else:
#       if not cur.right:
#         cur.right = TreeNode(val)
#         return root
#       cur = cur.right
