# Intuition

The problem "*[Reverse Linked List
](https://leetcode.com/problems/reverse-linked-list/)*" asks us to reverse a linked list.

# Approach

A linked list only has next pointers, therefore we are unable to simply look at any previous nodes. In order to

# Algorithm Steps

# Code

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        // use 3 pointers: cur, prev, & nxt
        ListNode cur = head;
        ListNode prev = null;

        while (cur != null) {
            // create temp to hold cur.next list values
            ListNode next = cur.next;

            // start reversing list
            cur.next = prev;

            // update ptrs each iteration
            prev = cur;
            cur = next;
        }
        return prev;
    }
}
```

# Complexity

- **Time Compplexity**: `O()`
- **Space Complexity**: `O()`
