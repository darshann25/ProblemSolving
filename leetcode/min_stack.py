# Review the following link for the question prompt: https://leetcode.com/problems/min-stack/

# O(N) time | O(1) space
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [float('inf')] 
        

    def push(self, x: int) -> None:
        if x <= self.minStack[-1]:
            self.minStack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()