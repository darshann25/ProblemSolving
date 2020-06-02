# Review the following link for the question prompt: https://leetcode.com/problems/reverse-linked-list/

# O(N) time | O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def reverseListRecursive(self, curr: ListNode) -> ListNode:
        
        if curr is None:
            return
        
        if curr.next is None:
            self.head = curr
            return
        
        self.reverseListRecursive(curr.next)
        curr.next.next = curr
        curr.next = None
            
    # Recursive Solution
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None: return head
        
        self.reverseListRecursive(head)
        return self.head
        
    
#     # Iterative Solution
#     def reverseList(self, head: ListNode) -> ListNode:
        
#         if head is None: return head
        
#         curr = head
#         prev = None
        
#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
            
#         return prev