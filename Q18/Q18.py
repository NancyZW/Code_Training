# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        first_iter = pHead
        second_iter = ListNode(0)
        second_iter.next = first_iter
        newHead = second_iter
        while first_iter is not None:
            nextNode = self.nextDiffNode(first_iter)
            if first_iter.next == nextNode:
                second_iter = first_iter
            else:
                second_iter.next = nextNode
            first_iter = nextNode
        return newHead.next

    def nextDiffNode(self,Node):
        while Node.next is not None:
            if Node.val == Node.next.val:
                Node = Node.next
            else:
                return Node.next
        return None
if __name__ == "__main__":
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(3)
    Node5 = ListNode(4)
    Node6 = ListNode(5)
    Node7 = ListNode(5)
    Node1.next = Node2; Node2.next = Node3
    Node3.next = Node4; Node4.next = Node5
    Node5.next = Node6; Node6.next = Node7
    sol = Solution()
    ans = sol.deleteDuplication(Node1)
    while ans is not None:
        print(ans.val)
        ans = ans.next

