# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# Input: head = [1,2]
# Output: false
 
# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        #find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the linked list in the second half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # now check for pallindrome
        firstList = head # first list starts at head
        secondList = prev #the second list(reversed list) starts at prev
        while secondList:
            if firstList.val != secondList.val:
                return False
            firstList = firstList.next
            secondList = secondList.next
        return True
                 