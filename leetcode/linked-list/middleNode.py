# Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
