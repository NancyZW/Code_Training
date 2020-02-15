# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minstack) == 0:
            self.minstack.append(node)
        elif self.minstack[-1] <= node:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(node)
    def pop(self):
        # write code here
        if len(self.stack) > 0:
            self.minstack.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if len(self.stack) > 0:
            return self.stack[-1]
    def min(self):
        # write code here
        if len(self.stack) > 0:
            return self.minstack[-1]

if __name__ == "__main__":
    sol = Solution()
    sol.push(1)
    # sol.push(0)
    # sol.push(5)
    print(sol.pop())
    print(sol.min())
    print(sol.top())