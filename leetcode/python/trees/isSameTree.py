# [Same Tree](https://leetcode.com/problems/same-tree/)
def isSameTree(self, p, q):
  """
  :type p: TreeNode
  :type q: TreeNode
  :rtype: bool
  """
  # base case: both trees are null
  if not p and not q:
      return True
  # one tree is null, the other isn't or the values of the nodes don't match
  if not p or not q or p.val != q.val:
      return False
  # recursion - return a bool if trees are the same of not
  return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
