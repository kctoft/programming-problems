# Intuition

The problem "*Maximum Twin Sum of a Linked List*" asks us to find the maximum sum of twin node values in an EVEN singly linked list. Essentially, we will be looking at the `head` and `n`th nodes at first to see what their sum is, then for each iteratio move the pointers inward to see what the twin sum is. However, looking back at a previous node is not possible in a SLL.

# Approach

- Option 1: use an additional data structure, such as an **array**, to store these values for easy searching using the **two pointer** technique (SC: `O(n)` memory).
- Option 2: If we are allowed to modify the LL, we can use TC: `O(1)` by reversing the one half of the LL.

### Option 1: Brute Force using an Array

#### Code

```python
# Brute Force using an array
# TC/SC: O(n)/O(n)
def pairSum(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: int
    """
    # create a list and init cur ptr to be referencing the head of the LL
    my_list = []
    cur = head
    # ontinue iterating until cur points to null
    while cur:
        my_list.append(cur.val)
        cur = cur.next

    # find the maximum value
    l = 0
    r = len(my_list) - 1
    res = 0
    while l < r:
        res = max(res, my_list[l] + my_list[r])
        l += 1
        r -= 1
    return res
```

### Option 2: Two Pointer & Reverse half of LL

#### Code

```python
# Using 2ptrs and rev LL
def pairSum(self, head):
  """
  :type head: Optional[ListNode]
  :rtype: int
  """
  # two pointer technique: fast & slow ptrs
  slow = head
  fast = head
  prev = None # help reverse the nodes

  # find the middle of the even LL
  while fast and fast.next:
      fast = fast.next.next # goes twice the speed
      temp = slow.next
      slow.next = prev # reverse
      prev = slow
      slow = temp

  # start summing twon values to find max value
  res = 0
  while slow:
      res = max(res, prev.val + slow.val)
      prev = prev.next
      slow = slow.next
  return res
```

# Complexity

- **Time Compplexity**: `O(n)` searching through the list 2x
- **Space Complexity**: `O(1)` constant memory
