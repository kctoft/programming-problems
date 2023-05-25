# Reverse Linked List
## Link: https://leetcode.com/problems/reverse-linked-list/

# Using the two pointer technique
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize prev pointer as NULL
        prev = None
        # Initialize the cur pointer as the head
        cur = head
        # Run a loop till cur points to NULL
        while cur:
            # Initialize next pointer as the next pointer of cur
            next = cur.next
            # Now assign the prev pointer to cur’s next pointer
            cur.next = prev
            # Assign cur to prev, next to cur
            prev = cur
            cur = next
        # Return the prev pointer to get the reverse
        return prev
