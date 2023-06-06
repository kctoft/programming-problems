# [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

# # iterative DFS:usiing a stack
# def kthSmallest(self, root, k):
#   """
#   :type root: TreeNode
#   :type k: int
#   :rtype: int
#   """
#   # base case: root is null
#   if not root:
#     return
#   # start search traversal: in-order
#   # create a stack to keep track of visited nodes
#   stack = []
#   curr = root
#   # iteratively search the left then right subtree
#   while stack or curr:
#       while curr:
#           stack.append(curr)
#           curr = curr.left
#       curr = stack.pop()
#       k -= 1
#       if k == 0:
#           return curr.val
#       curr = curr.right



# recursive DFS: a in-order traversal of a BST will give us a sorted list
def kthSmallest(self, root, k):
  """
  :type root: TreeNode
  :type k: int
  :rtype: int
  """
  stack = []

  def inorder(root):
    # base case: root is null
    if not root:
      return
    # start search on left subtree, then the right
    inorder(root.left)
    stack.append(root.val)
    inorder(root.right)
    return

  inorder(root) # preform recursive dfs in-order traversal
  return stack[k-1] # return the first node from th e sorted list
