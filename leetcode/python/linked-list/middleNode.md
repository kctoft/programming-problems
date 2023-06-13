# Intuition

The problem "*Middle of the Linked List*" asks us to find the middle node of a singly linked list. My first intuition was to use **two pointers**, mv the **fast and slow pointer** technique, in order to traverse the list.

# Approach

Initialize both the `slow` and `fast` pointers to the head of the linked list. For each iteration, the `slow` pointer moves one node at a time and the `fast` pointer moves two nodes each iteration.

![Fast & Slow](./fastSlow.gif)

By the time the `fast` pointer has reached the end of the list, the `slow` pointer will have traversed up until the middle of the list as goes half the speed of the `fast` pointer.

# Code

```python
def middleNode(self, head):
  """
  :type head: ListNode
  :rtype: ListNode
  """
  # use the Fast & Slow Pointers Technique
  slow = head
  fast = head

  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  return slow
```

# Complexity

- **Time Compplexity**: `O(n)` where `n` is the number of nodes of the linked list
- **Space Complexity**: `O(1)` since we are using constant time to search through the list
