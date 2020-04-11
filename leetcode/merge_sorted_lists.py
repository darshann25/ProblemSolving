"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Recursive Solution
    def mergeTwoLists(self, l1, l2):

        # Check if both lists are empty
        if not (l1 and l2):
            return l1 or l2
        # Check which value is smaller and move it ot l1
        elif l1.val > l2.val:
            l1, l2 = l2, l1

        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # Iterative Solution
    def mergeTwoListsIterative(self, l1, l2):

        if not l1 and not l2:
            return l1

        self.head = ListNode(-1,-1)
        curr = self.head

        while l1 or l2:

            if not l1:
                curr.next = l2
                break
            elif not l2:
                curr.next = l1
                break
            else:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

        return self.head.next
