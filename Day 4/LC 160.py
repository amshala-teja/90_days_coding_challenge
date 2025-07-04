# 160. Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
# If you correctly return the intersected node, then your solution will be accepted.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # will make use of hashset. put all the elements of headB in a set and check whether the elements are in the set using headA, return the firs telement found.
        # Approach1 :
        visited = set()
        currB = headB

        while currB:
            visited.add(currB)
            currB = currB.next
        currA = headA
        while currA:
            if currA in visited:
                return currA
            currA = currA.next
        return None
        # Time Complexity: O(m + n)
        # Traverses both lists once.
        # Space Complexity: O(n)
        # You store all nodes of list B in a set.
# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
# Approach2: 
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
        # Time Complexity: O(m + n)
        # space Complexity: O(1)

#Approach:
# By switching the heads when reaching the end, both pointers cover the same total distance:
    # First list length + second list length.
    # If the lists intersect, they will meet at the intersection node.
    # If not, both pointers will reach None simultaneously.