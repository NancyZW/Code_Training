# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code
        if root is None:
            return '#'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        s_list = s.split(',')
        return self.subDeserialize(s_list)

    def subDeserialize(self,s_list):
        if len(s_list) == 0:
            return None
        node = s_list.pop(0)
        if node == "#":
            return None
        root = TreeNode(int(node))
        root.left = self.subDeserialize(s_list)
        root.right = self.subDeserialize(s_list)
        return root

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node2.left = node4
    node1.right = node3
    node3.left = node5
    node3.right = node6

    sol = Solution()
    ans = sol.Serialize(node1)
    print(ans)

    ans2 = sol.Deserialize(ans)
    print(ans2.val)
    print(ans2.left.val)
    print(ans2.right.val)
    print(ans2.left.left.val)
    print(ans2.right.left.val)
    print(ans2.right.right.val)
