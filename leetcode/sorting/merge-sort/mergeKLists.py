# Merge k Sorted Lists
## Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Merege all of the linked-lists into one sorted LL and return it.

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
        # list is null or len zero
        if not lists or len(lists) == 0:
            return None

        # merge sort: divide
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # ensure that list 2 could be null
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # conquer & combine
                mergedLists.append((self.mergeTwoLL(l1, l2)))
            lists = mergedLists
        return lists[0]

    # helperfucn: merge two lisnked lists
    def mergeTwoLL(self, l1, l2):
        dummy = ListNode()
        tail = dummy



        # case 1: continue to iterate while lists are non-null
        while l1 and l2:
            # is l1 is smaller, use it first then move forward
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # update pointer for tail
            tail = tail.next

        # case 2: one list is or become null
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
