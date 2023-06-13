# [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

# iterative DFS
# def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         stack = [[root, 1]]
#         res = 0
#         while stack:
#               node, depth = stack.pop()
#               if node:
#                     res = max(res, depth)
#                     stack.append([node.left, depth + 1])
#                     stack.append([node.right, depth + 1])
#         return res


# use DFS & recursion to find max depth
def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # base case: check if root is null
        if not root:
            return 0 # empty tree has a depth of zero
        # recursion TC/SC : O(n)/O(n)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# use BFS to search for max depth
# def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # base case: check if root is null
#         if not root:
#             return 0 # empty tree has a depth of zero
#         # BFS
#         lvl = 0
#         q = deque([root])
#         while q:
#           # traverse the entire level
#           for i in range(len(q)):
#             node = q.popleft()
#             if node.left:
#               q.append(node.left)
#             if node.right:
#               q.append(node.right)
#           lvl += 1
#         return lvl
