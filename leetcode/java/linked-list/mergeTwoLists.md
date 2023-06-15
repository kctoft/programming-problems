# Intuition

The problem "*[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)*" asks us to merge two sorrted linked lists as a single list.

Since the lists are already sorted, we

# Approach

# Algorithm Steps

# Code

First implementation using **brute force** with a loop and saving the resultant into a final list.

```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
  // create a res list to return
  final ListNode root = new ListNode();
  ListNode prev = root;
  // base case: both of the lists non-null
  while (list1 != null && list2 != null) {
    // if both are non-null, which head is larger?
    // case 1: list2's value is larger
    if (list1.val < list2.val) {
      prev.next = list1;
      list1 = list1.next;
    } else {
        // case 2: list1's value is larger
        prev.next = list2;
        list2 = list2.next;
    }
    // increment by 1
    prev = prev.next;
  }
  // check if one list runs out, supply it with the remainder of the other
  prev.next = list1 != null ? list1 : list2;
  return root.next;
}
```

This next implmentation uses **recursion**  with parameters being the

```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
  if (list1 == null) return list2;
  if (list2 == null) return list1;

  if (list1.val < list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list2.next, list1);
    return list2;
  }
}
```

# Complexity

- **Time Compplexity**: `O(n)`, where `n` is the number of nodes in the list.
- **Space Complexity**: `O(1)` scine we only use one data structure.
