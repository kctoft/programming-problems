# Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
def levelOrder(self, root):
      """
      :type root: TreeNode
      :rtype: List[List[int]]
      """
      # init empty queue and res list
      res = []
      q = collections.deque()
      # if root is non-null, add it to queue
      if root:
          q.append(root)

      # while non-null, add the corresponding subtrees lvl by lvl
      while q:
          lvl = []
          # for every node on this level, add them to the queue
          for i in range(len(q)):
              node = q.popleft()
              lvl.append(node.val)
              # for each element on the current lvl, add their children to the queue
              if node.left:
                  q.append(node.left)
              if node.right:
                  q.append(node.right)
          # add cur lvl to the res list
          res.append(lvl)
      # return res list
      return res
