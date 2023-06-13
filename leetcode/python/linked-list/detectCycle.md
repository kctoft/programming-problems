# Intuition

The problem "*[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)*" asks us to determine if there is a cycle in the linked list. If a cycle is found, return the node where the cycle begins. Otherwise, return `None`.

For problems like these, using two pointers, a `fast` and `slow` pointer, (i.e., **Floyd's Cycle algorithm**), can help us detect a cycle.

## Floyd's Cycle Algorithm

- Alternative name is the **Tortoise-Hare** algorithm
- Using two pointers, a `slow` and `fast` pointer, both initialized at the head.
- `fast` pointer travels 2x (or some multiple) speed faster than the slow pointer
- A cycle is detected when `fast` catches up with `slow`
- No cycle is detected when `fast` pointer reaches the end of the lsit, e.g., `fast.next` points to `None`

# Approach

When the two pointers meet, we know that there is a cycle in the linked list.
We then reset the slow pointer to the head of the linked list and move both pointers at the same pace, one step at a time, until they meet again.
The node where they meet is the starting point of the cycle.
If there is no cycle in the linked list, the algorithm will return null.

# Algorithm Steps

1. Initialize both `slow` & `fast` pointer to the head node
1. Traverse the list iteratively, fast pointer goes 2x the speed of the slow pointer
1. If the pointers meet, there is a cycle in the linked list. Reset the slow pointer to the head of the linked list, and move both pointers one step at a time until they meet again. The node where they meet is the starting point of the cycle.
1. If the fast pointer reaches the end of the list without meeting the slow, there is no cycle in the linked list. Return None.

# Code

```python
def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize both `slow` & `fast` pointer to the head node
        slow, fast = head, head
        # Traverse the list iteratively, fast pointer goes 2x the speed of the slow pointer (Floyd's Cycle Algorithm)
        # either the pointers will meet up and a cycle is formed, or there is no cycle
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          # If the pointers meet, there is a cycle in the linked list. Reset the slow pointer to the head of the linked list, and move both pointers one step at a time until they meet again. The node where they meet is the starting point of the cycle.
          if slow == fast:
            slow = head
            while slow != fast:
              slow = slow.next
              fast = fast.next
            #  cycle is found
            return slow
        # If the fast pointer reaches the end of the list without meeting the slow, there is no cycle in the linked list. Return None.
        return None
```

# Complexity

- **Time Compplexity**: `O(n)`,  where `n` is the number of nodes in the linked list. In the worst case scenario, we will need to traverse the entire list to determine if there is a cycle.
- **Space Complexity**: `O(1)`, as we are only using two pointers and not using any additional data structures.
