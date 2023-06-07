# [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

def isSubtree(self, root, subRoot):
  """
  :type root: TreeNode
  :type subRoot: TreeNode
  :rtype: bool
  """
  # check if trees are empty
  if not subRoot: return True
  if not root: return False

  if self.sameTree(root, subRoot):
    return True
  return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


  # helper fcn to determine if same tree
  def sameTree(self, root, subRoot):
    # both root values are null
    if not root and not subRoot:
      return True
    # both trees are non-null & have the same value for root
    if root and subRoot and root.val == subRoot.val:
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
  return False
