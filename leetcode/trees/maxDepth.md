# Intuition

The problem "*[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)*" asks us to return the maximum depth of the tree given its root.

# Approach

To find the "maximum depth" of a binary tree is to find the furthest node from the root in the BST. Therefore, we will search the left subtree and right subtree, recursively.

# Algorithm Steps

1. Check for the base case: If the root is null, return a depth of zero.
1. Return the maximum value between the `right` and `left` subtree (include +1 since this is 0-indexed)

# Code

```python
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
```

# Complexity

- **Time Compplexity**: `O(n)`, where `n` is the height of the tree
- **Space Complexity**: `O(n)`, where `n` is the height of the tree
