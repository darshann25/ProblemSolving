# Review the following link for the question prompt: https://leetcode.com/problems/merge-k-sorted-lists/

# O(n * m log(m)) time | O(N) space, where n is the average length of sorted list, m is number of lists, N is total length of all lists combined

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        
        head = ListNode(-1)
        node = head
        
        orgList = lists.copy()
        lists = []
        for n in orgList:
            if n is not None:
                lists.append(n)
        
        while len(lists) != 0:
            lists.sort(key = lambda x : x.val)
            node.next = ListNode(lists[0].val)
            lists[0] = lists[0].next
            if lists[0] is None: del lists[0]
            node = node.next
            
        return head.next