# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead = ListNode(-1)
        piter = pHead
        iter1 = pHead1
        iter2 = pHead2
        while iter1 is not None and iter2 is not None:
            if iter1.val <= iter2.val:
                piter.next = iter1
                iter1 = iter1.next
            else:
                piter.next = iter2
                iter2 = iter2.next
            piter = piter.next
        if iter1 is None:
            piter.next = iter2
        if iter2 is None:
            piter.next = iter1
        return pHead.next

    def Merge2(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge2(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge2(pHead1,pHead2.next)
            return pHead2



if __name__ == "__main__":
    pHead1 = ListNode(-1)
    n1 = pHead1
    for i in range(1,10,2):
        node1 = ListNode(i)
        n1.next = node1
        n1 = node1
    n1 = pHead1
    pHead2 = ListNode(0)
    n2 = pHead2
    for i in range(2, 4, 2):
        node2 = ListNode(i)
        n2.next = node2
        n2 = node2
    n2 = pHead2

    while n1 is not None:
        # print(n1.val)
        n1 = n1.next
    while n2 is not None:
        # print(n2.val)
        n2 = n2.next
    sol = Solution()
    n = sol.Merge2(pHead1,pHead2)
    while n is not None:
        print(n.val)
        n = n.next
