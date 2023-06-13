# Linked List Cycle II
# Link: https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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
