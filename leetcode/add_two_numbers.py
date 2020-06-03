# Review the following link for the question prompt: https://leetcode.com/problems/add-two-numbers/

# O(N) time | O(N) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(-1)
        node = head
        currSum = 0
        carry = 0
        
        while l1 or l2 or carry != 0:
            
            if not l1 and not l2:
                currSum = carry
            elif not l2:
                currSum = l1.val + carry
            elif not l1:
                currSum = l2.val + carry
            else:
                currSum = (l1.val + l2.val + carry)
            print(currSum)
            
            carry = int(currSum / 10)
            node.next = ListNode(int(currSum % 10))
            print(carry, node.next.val)
            
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return head.next