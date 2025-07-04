# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        d = ListNode(0)
        d.next = head
        curr = head
        len = 0
        prev = d
        while curr:
            curr = curr.next
            len += 1
        prevPos = len - n
        for i in range(prevPos):
            prev = prev.next
        prev.next = prev.next.next
        return d.next


# Two pointer approach
# This solution uses the two-pointer technique (fast and slow pointer) to efficiently remove the N-th node from the end in one pass.
# Steps:
        # Create a dummy node that points to the head of the list. This helps handle edge cases cleanly, like when the head needs to be removed.
        # Initialize two pointers:
        # ahead (fast pointer)
        # behind (slow pointer)
        # Move the ahead pointer n+1 steps forward to maintain a gap of n nodes between ahead and behind.
        # Move both pointers one step at a time until ahead reaches the end of the list.
        # At this point, behind is just before the node that needs to be removed.
        # Skip the target node by setting behind.next = behind.next.next.
        # Return the updated list starting from d.next.


        d = ListNode(0)
        d.next = head
        ahead = behind = d
        for _ in range(n+1):
            ahead = ahead.next
        while ahead:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return d.next


