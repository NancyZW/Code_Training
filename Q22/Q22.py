# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        n = head
        listlength = 0
        while n is not None:
            listlength += 1
            n = n.next
        if k > listlength:
            return None
        t = listlength - k
        kthNode = head
        while t > 0:
            kthNode = kthNode.next
            t -= 1
        return kthNode

    def FindKthToTail2(self, head, k):
        if k == 0:
            return None
        iter_right = head
        iter_left = head
        idx = 1
        while iter_right is not None and idx < k:
            iter_right = iter_right.next
            idx += 1
        if iter_right is None:
            return None
        while iter_right.next is not None:
            iter_right = iter_right.next
            iter_left = iter_left.next
        return iter_left
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(0)
    node_list = [head]
    for i in range(1,5):
        node = ListNode(i)
        node_list.append(node)
    for i in range(len(node_list)-1):
        node_list[i].next = node_list[i+1]

    ans = sol.FindKthToTail2(head,0)
    print(ans.val)