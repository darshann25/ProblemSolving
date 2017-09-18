"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, node, partition):
        beforeStart = None
        beforeEnd = None
        afterStart = None
        afterEnd = None

        while node != None :
            nextNode = node.next
            node.next = None

            if node.val < partition:
                if beforeStart == None:
                    beforeStart = node
                    beforeEnd = beforeStart
                else:
                    beforeEnd.next = node
                    beforeEnd = beforeEnd.next
            else:
                if afterStart == None:
                    afterStart = node
                    afterEnd = afterStart
                else:
                    afterEnd.next = node
                    afterEnd = afterEnd.next

            node = nextNode

        if beforeStart == None:
            return afterStart

        beforeEnd.next = afterStart

        return beforeStart

s = Solution()

list = [1, 4, 3, 2, 5, 2]
head = ListNode(list[0])
node = head

for i in range(len(list)):
    node.next = ListNode(list[i+1])
    node = node.next
