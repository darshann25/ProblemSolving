"""

Given a pre-order traversal, construct a binary search tree in O(n) time.

"""


class Node(int):
    val = -1

    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Solution:
    def buildTreeFromPreOrderList(self, list):
        stack = Stack()
        root = Node(list[0])
        stack.push(root)
        index = 1

        while index < len(list):
            if not stack.isEmpty() and stack.peek() > list[index]:
                temp = Node(list[index])
                stack.peek().left = temp
                stack.push(temp)
                index += 1
            else:
                temp = None
                while not stack.isEmpty() and stack.peek() < list[index]:
                    temp = stack.pop()
                temp1 = Node(list[index])
                temp.right = temp1
                stack.push(temp1)
                index += 1

        return root


s = Solution()
l = [4, 2, 1, 3, 6, 5, 7]
root = s.buildTreeFromPreOrderList(l)

res = [root.val]

left = root.left
res.append(left.val)
res.append(left.left.val)
res.append(left.right.val)
right = root.right
res.append(right.val)
res.append(right.left.val)
res.append(right.right.val)

assert res == l, "Houston, we have a problem!"
print "Success!"
