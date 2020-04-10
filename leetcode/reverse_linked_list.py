"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time Complexity: 0(n)
# Space Complexity: 0(1)
class Solution:

    # Recursive Solution
    def reverseListRecursive(self, curr):

        if curr is None:
            return

        if curr.next is None:
            self.head = curr
            return

        self.reverseListRecursive(curr.next)
        curr.next.next = curr
        curr.next = None

    def reverseListR(self, head):

        if head is None: return head

        self.reverseListRecursive(head)
        return self.head

    # Iterative Solution
    def reverseList(self, head):

        if head is None: return head

        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
