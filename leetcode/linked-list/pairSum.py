# Maximum Twin Sum of a Linked List
## Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# TC/SC: O(n)/O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Brute Force using an array
# # TC/SC: O(n)/O(n)
# def pairSum(self, head):
#     """
#     :type head: Optional[ListNode]
#     :rtype: int
#     """
#     # create a list and init cur ptr to be referencing the head of the LL
#     my_list = []
#     cur = head
#     # ontinue iterating until cur points to null
#     while cur:
#         my_list.append(cur.val)
#         cur = cur.next

#     # find the maximum value
#     l = 0
#     r = len(my_list) - 1
#     res = 0
#     while l < r:
#         res = max(res, my_list[l] + my_list[r])
#         l += 1
#         r -= 1
#     return res

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
