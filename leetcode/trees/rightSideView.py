# [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)
def rightSideView(self, root):
  """
  :type root: TreeNode
  :rtype: List[int]
  """
  # base case:
  if not root:
      return []
  # create a res list to return and a queue for FIFO popping
  res = []
  q = collections.deque([root])
  # use BFS to traverse lvl by lvl
  while q:
    right_elements = None
    # at each lvl, append children to the queue
    for _ in range(len(q)):
      node = q.popleft()
      if node:
        right_elements = node
        q.append(node.left)
        q.append(node.right)
    # add only right most elements of each lvl to queue
    if right_elements:
      res.append(right_elements.val)
  # return modified list
  return res
