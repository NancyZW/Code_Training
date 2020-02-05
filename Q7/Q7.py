# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None

        val = pre.pop(0)
        Root = TreeNode(val)
        root_loc = tin.index(val)
        leftNode = tin[:root_loc]
        RightNode = tin[root_loc+1:]
        # print(val)
        # print("pre:",pre)
        # print("leftNode:",leftNode)
        # print("RightNode:",RightNode)
        Root.left = Solution().reConstructBinaryTree(pre, leftNode)
        Root.right = Solution().reConstructBinaryTree(pre, RightNode)

        return Root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
ans = Solution().reConstructBinaryTree(pre, tin)
print(ans.val)