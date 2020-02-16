# -*- coding:utf-8 -*-
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        path = []
        tmppath = []
        self.GetPath(root, expectNumber, path, tmppath)
        return path

    def GetPath(self, root, expectNumber, path, tmppath):
        tmppath.append(root.val)
        if root.val == expectNumber and root.left is None and root.right is None:
            onepath = copy.deepcopy(tmppath)
            path.append(onepath)
        if root.val < expectNumber and root.left is not None:
            self.GetPath(root.left, expectNumber-root.val, path, tmppath)
        if root.val < expectNumber and root.right is not None:
            self.GetPath(root.right, expectNumber - root.val, path, tmppath)
        tmppath.pop()


if __name__ == "__main__":
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(12)
    node3 = TreeNode(4)
    node4 = TreeNode(7)
    # node5 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    # node2.right = node5

    sol = Solution()
    val = sol.FindPath(root, 22)
    print(val)