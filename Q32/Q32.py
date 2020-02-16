# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        list = [root]
        val = []
        while len(list):
            node = list.pop(0)
            val.append(node.val)
            if node.left is not None:
                list.append(node.left)
            if node.right is not None:
                list.append(node.right)
        return val


if __name__ == "__main__":
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    sol = Solution()
    val = sol.PrintFromTopToBottom(root)
    print(val)
