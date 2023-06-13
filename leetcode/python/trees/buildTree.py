# [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
def buildTree(self, preorder, inorder):
  """
  :type preorder: List[int]
  :type inorder: List[int]
  :rtype: TreeNode
  """
  # base case: emptry BST
  if not preorder or not inorder:
      return None
  # first val in pre-order is the root node
  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])
  # build subtree recursively using sublists
  root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
  root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
  return root
