#  Linked List Cycle
# link: https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # Flyod's Cycle Algorithm
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    # edge case: if next ptr is null return False
    return False
