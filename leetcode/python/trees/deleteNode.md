# Intuition

The problem "*[Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)*" asks us to delete a particular node from a BST if it exists.

# Approach

The problem provides a hint to divide it into two steps:

1. Search for the node to remove using BST
1. if the node exists, safely remove it

# Algorithm Steps

1. Base case: Check if the `root` is `None`, return `None`
1. If the `key` to be deleted/removed is less than the `root`'s `key`, then recursively call the `deleteNode` function with the `left` subtree as the new `root`.
1. If the `key` to be deleted/removed is greater than the `root`'s `key`, then recursively call the `deleteNode` function with the `right` subtree as the new `root`.
1. If the `key` to be deleted is equal to the `root`'s `key` we have found match:
  a. If the `root` has no children or only has one child, repalce the `root` with its child (if it has any).
  b. If the `root`has two children, find the **in-order** successor of the `root` (i.e., the smallest key in the subtree). Set the value of the `root` to be the value of its **in-order** successor from thr `right` subtree
1. Return the modifued `root`

# Code

```python
def deleteNode(self, root, key):
  """
  :type root: TreeNode
  :type key: int
  :rtype: TreeNode
  """
  # Base case: If the root is None, return None
  if not root:
    return None

  # If the key to be deleted is less than the root's key,
  # then the function is recursively called with the left subtree
  if key < root.val:
    root.left = self.deleteNode(root.left, key)
  # If the key to be deleted is greater than the root's key,
  # then the function is recursively called with the right subtree
  elif key > root.val:
    root.right = self.deleteNode(root.right, key)
  else:
    # Case 1: If the root has no children or only one child, then the root is replaced with its child
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    # Case 2: If the root has two children, then the in-order successor of the root is found
    else:
      cur = root.right
      while cur.left:
          cur = cur.left
      # The value of the in-order successor is copied to the root
      root.val = cur.val
      # The in-order successor is then deleted from the right subtree of the root
      root.right = self.deleteNode(root.right, cur.val)

  return root
```

# Complexity

- **Time Compplexity**: `O(n)`, where `n` is the height of the tree (worst case)
- **Space Complexity**: `O(n)`, where `n` is the height of the tree
