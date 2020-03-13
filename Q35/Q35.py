# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        newpHead = RandomListNode(pHead.label)
        newpHead.next = self.Clone(pHead.next)
        newpHead.random = pHead.random
        return newpHead

if __name__ == "__main__":
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node1.next = node2
    node1.random = node3
    node2.next = node3
    node2.random = node3
    node3.random = node3

    sol = Solution()
    newpHead = sol.Clone(node1)
    while newpHead is not None:
        print(newpHead.label,newpHead.random.label)
        newpHead = newpHead.next
