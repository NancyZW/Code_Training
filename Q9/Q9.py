# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        # print(self.stack1)
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1.pop())
        # print(self.stack2)
        ans = self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return ans

sol = Solution()
sol.push(1)
sol.push(2)
sol.push(3)
print(sol.pop())
print(sol.pop())
print(sol.pop())


