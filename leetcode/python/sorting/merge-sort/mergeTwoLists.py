# Merge Two Sorted Lists
## https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
        tail = dummy

        # iterate while both list1 and list2 are non-null
        while list1 and list2:
            # check to see which head is smaller
            if list1.val < list2.val:
                # insert to tail
                tail.next = list1
                # update pointer
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # update tail pointer
            tail = tail.next

        # special case: either list still has nodes (i.e. non-null)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
