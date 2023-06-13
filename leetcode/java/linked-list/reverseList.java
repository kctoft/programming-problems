// [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)
public ListNode reverseList(ListNode head) {
    ListNode cur = head;
    ListNode prev = null;

    while (cur != null) {
        ListNode nxt = cur.next;
        cur.next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

