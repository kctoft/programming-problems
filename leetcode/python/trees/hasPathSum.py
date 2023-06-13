# [Path Sum](https://leetcode.com/problems/path-sum/)
def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # BS not BST: meaning search all nodes
        # BFS: level-by-level search
        # base case: check if root is NULL
        if not root:
            return False
        # check: is leaf node -> does the sum match the target?
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.right, targetSum - root.val) or self.hasPathSum(root.left, targetSum - root.val)
