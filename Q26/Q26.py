# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        return self.HasSubtreeCore(pRoot1,pRoot2) or self.HasSubtreeCore(pRoot1.left,pRoot2) or self.HasSubtreeCore(pRoot1.right,pRoot2)

    def HasSubtreeCore(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.HasSubtreeCore(pRoot1.left,pRoot2.left) and self.HasSubtreeCore(pRoot1.right,pRoot2.right)
        else:
            return False

if __name__ == "__main__":
    pRoot1 = TreeNode(8)
    node1 = TreeNode(8)
    node2 = TreeNode(9)
    node3 = TreeNode(2)
    node4 = TreeNode(7)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    pRoot1.left = node1
    pRoot1.right = node4
    node1.left = node2
    node1.right = node3
    node3.left = node5
    node3.right = node6

    pRoot2 = TreeNode(8)
    node5 = TreeNode(9)
    node6 = TreeNode(2)
    pRoot2.left = node5
    pRoot2.right = node6

    sol = Solution()
    ans = sol.HasSubtree(pRoot1,pRoot2)
    print(ans)