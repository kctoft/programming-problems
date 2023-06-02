#  Merge K Sorted Lists
#  Link: https://leetcode.com/problems/merge-k-sorted-lists/submissions/961247618/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    # special edge case: lists is null or 0
    if not lists or len(lists) == 0: return None

    # merge sort: divide up the lists into sub problems
    # while there is at least 2 lists
    while len(lists) > 1:
        # enpty list to append sorted values to
        mergedLists = []

        # for every iteration, range[start,stop,step]
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # ensure that list 2 could be null/empty
            l2 = lists[i + 1] if (i + 1) < len(lists) else None

            # conquer & combine
            mergedLists.append(self.mergeTwoLL(l1, l2))

        # update the return value
        lists = mergedLists

    return lists[0]

# helper function; merge two linked lists
# merge sort algorithm
def mergeTwoLL(self, l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next
