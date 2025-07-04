# 876. Middle of the Linked List
#  a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
# finding length method;
        # curr = head
        # if not curr:
        #     return head
        # length = 0
        # while curr:
        #     length+=1
        #     curr = curr.next
        # mid = length//2
        # curr = head
        # for _ in range(mid):
        #     curr = curr.next
        # return curr
#fast and slow pointer method
# here when the fast pointer reaches the end of the length, slow pointer will be in the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
