class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def returnLinkedListAsList(self):
        node = self
        list = []

        while node is not None:
            list.append(node.val)
            node = node.next

        return list


def createLinkedList(list):
    node = ListNode(list[0])
    head = node
    list.pop(0)

    for value in list:
        if node.next is None:
            node.next = ListNode(value)

        node = node.next

    return head
