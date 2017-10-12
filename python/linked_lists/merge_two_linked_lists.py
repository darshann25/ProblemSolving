"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :
  5 -> 8 -> 20
  4 -> 11 -> 15

The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"""
from list_node import ListNode
from list_node import createLinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        sorted = ListNode(-1)
        head = sorted

        while not A is None or not B is None:
            if A is None:
                if not sorted: return B
                else:
                    sorted.next = B
                    break

            if B is None:
                if not sorted: return A
                else:
                    sorted.next = A
                    break

            if A.val < B.val:
                if sorted is None:
                    sorted = A
                else:
                    sorted.next = A
                    sorted = sorted.next
                A = A.next
            else:
                if sorted is None:
                    sorted = B
                else:
                    sorted.next = B
                    sorted = sorted.next
                B = B.next

        return head.next

s = Solution()
A = createLinkedList([5, 8, 20])
B = createLinkedList([4, 11, 15])
expResult = [4, 5, 8, 11, 15, 20]
result = s.mergeTwoLists(A, B)
assert result.returnLinkedListAsList() == expResult, "Houston, we have a problem!"
print "Success!"
