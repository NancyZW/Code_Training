# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        pre = None
        node = pHead
        while node.next is not None:
            next = node.next
            node.next = pre
            pre = node
            node = next
        node.next = pre
        return node

if __name__ == "__main__":
    pHead = ListNode(0)
    n = pHead
    for i in range(1,10):
        node = ListNode(i)
        n.next = node
        n = node
    n = pHead
    sol = Solution()
    n = sol.ReverseList(n)
    while n is not None:
        print(n.val)
        n = n.next
