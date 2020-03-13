# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        # print(pRootOfTree.val)
        pRootleft = self.Convert(pRootOfTree.left)
        pRootright = self.Convert(pRootOfTree.right)
        thisHead = pRootOfTree
        if pRootleft is not None:
            thisHead = pRootleft
            while pRootleft.right is not None:
                pRootleft = pRootleft.right
            pRootOfTree.left = pRootleft
            pRootleft.right = pRootOfTree
        else:
            pRootOfTree.left = None
        if pRootright is not None:
            pRootright.left = pRootOfTree
            pRootOfTree.right = pRootright
        else:
            pRootOfTree.right = None
        # while thisHead.left is not None:
        #     thisHead = thisHead.left
        # if pRootOfTree is None and pRootleft is None:
        #     print('None','None')
        # elif pRootOfTree is None:
        #     print('None', pRootleft.val)
        # elif pRootleft is None:
        #     print(pRootOfTree.val, "none")
        # else:
        #     print(pRootOfTree.val,pRootleft.val)
        return thisHead

if __name__ == "__main__":
    node1 = TreeNode(10)
    node2 = TreeNode(6)
    node3 = TreeNode(4)
    node4 = TreeNode(8)
    node5 = TreeNode(14)
    node6 = TreeNode(12)
    node7 = TreeNode(16)
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.left = node6
    node5.right = node7

    sol = Solution()
    head = sol.Convert(node1)
    tail = head
    while head is not None:
        print(head.val)
        if head.right is None:
            tail = head
        head = head.right

    while tail is not None:
        print(tail.val)
        tail = tail.left
