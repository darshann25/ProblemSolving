# Review the following link for the question prompt: https://leetcode.com/problems/reverse-nodes-in-k-group/

# O(N) time | O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        counter = k
        node = head
        start = node
        end = None
        head = None
        
        while node is not None:
            
            if counter != 1:
                counter -= 1
                node = node.next
            end = node
            if node is None: break
            
            if counter == 1:
                newStart = node.next if node is not None else node
                start, end = self.reverseList(start, end)
                if head is None: 
                    head = start
                else:
                    prevEnd.next = start

                end.next = newStart
                start = newStart
                node = end
                prevEnd = end
                end = None
                counter = k + 1

                
        if end is not None:
            start, end = reverseList(start, end)
            end.next = None
        
        return head
    
    def reverseList(self, start, end):
        
        newEnd = start
        newStart = None
        end.next = None
        
        currNode = start
        prevNode = None

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        newStart = prevNode
        
        return newStart, newEnd