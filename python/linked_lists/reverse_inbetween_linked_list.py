# coding=utf-8
""""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
"""

from list_node import createLinkedList

def setNode(A, pos):
    if pos < 0: return None
    for i in range(pos - 1):
        if A is None: return None
        A = A.next
    return A


class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n: return A

        start = setNode(A, m)
        node = setNode(A, m + 1)
        end = setNode(A, n)
        tail = setNode(A, n + 1)

        if m - 1 > 0:
            begin = setNode(A, m - 1)
        else:
            begin = None

        while tail is not end:
            start.next = tail
            tail = start
            start = node
            if node is not None and node.next is not None: node = node.next

        if begin is not None:
            begin.next = end
            head = A
        else:
            head = tail

        return head

s = Solution()
list = [1, 2, 3, 4, 5, 6, 7]
exp_res = [1, 2, 6, 5, 4, 3, 7]
node = createLinkedList(list)

node = s.reverseBetween(node, 3, 6)
res = node.returnLinkedListAsList()
assert res == exp_res, "Houston, we have a problem!"
print "Succcess!"
