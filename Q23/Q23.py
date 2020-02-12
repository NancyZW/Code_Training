# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return None
        iter_left = pHead
        iter_right = pHead.next
        while iter_left != iter_right:
            iter_left = iter_left.next
            iter_right = iter_right.next.next

        cycle_lenth = 1
        while iter_left.next != iter_right:
            iter_left = iter_left.next
            cycle_lenth += 1

        iter_right = pHead
        for i in range(cycle_lenth):
            iter_right = iter_right.next

        iter_left = pHead
        while iter_left != iter_right:
            iter_left = iter_left.next
            iter_right = iter_right.next
        return iter_right

if __name__ == "__main__":
    sol = Solution()
    pHead = ListNode(0)
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)
    Node5 = ListNode(5)
    pHead.next = Node1; Node1.next = Node2
    Node2.next = Node3; Node3.next = Node4
    Node4.next = Node5; Node5.next = Node3
    ans = sol.EntryNodeOfLoop(pHead)
    print(ans.val)