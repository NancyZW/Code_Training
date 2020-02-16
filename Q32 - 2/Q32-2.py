# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        ans = []
        # val = []
        stack1 = [pRoot]
        stack2 = []
        while len(stack1) or len(stack2):
            if len(stack2) == 0:
                val = []
                while len(stack1) != 0:
                    node = stack1.pop()
                    val.append(node.val)
                    if node.left is not None:
                        stack2.append(node.left)
                    if node.right is not None:
                        stack2.append(node.right)
                ans.append(val)
            elif len(stack1) == 0:
                val = []
                while len(stack2) != 0:
                    node = stack2.pop()
                    val.append(node.val)
                    if node.right is not None:
                        stack1.append(node.right)
                    if node.left is not None:
                        stack1.append(node.left)
                ans.append(val)
        return ans

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
    val = sol.Print(root)
    print(val)
