# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        while root is None:
            return None
        left = root.left
        right = root.right
        root.left = self.Mirror(right)
        root.right = self.Mirror(left)
        return root





if __name__ == "__main__":
    pRoot = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(10)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(9)
    node6 = TreeNode(11)
    pRoot.left = node1
    pRoot.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    sol = Solution()
    root = sol.Mirror(pRoot)
    list = [root]
    while len(list)!=0:
        root = list.pop(0)
        if root is not None:
            print(root.val)
            list.append(root.left)
            list.append(root.right)


    # print(ans)