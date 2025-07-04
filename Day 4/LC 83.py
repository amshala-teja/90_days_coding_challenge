# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
# Time complexity: O(n) where n is the number of nodes in the linked list.
# Space complexity: O(1) since we are not using any extra space.