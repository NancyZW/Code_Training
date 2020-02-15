# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code
        if pRoot is None:
            return True
        preorder = self.preorder(pRoot)
        sympreorder = self.sympreorder(pRoot)
        return (preorder == sympreorder)

    def preorder(self, pRoot):
        preorder = []
        list = [pRoot]
        while len(list) != 0:
            root = list.pop()
            if root is not None:
                preorder.append(root.val)
                list.append(root.right)
                list.append(root.left)
            else:
                preorder.append(root)
        return preorder
    def sympreorder(self, pRoot):
        sympreorder = []
        list = [pRoot]
        while len(list) != 0:
            root = list.pop()
            if root is not None:
                sympreorder.append(root.val)
                list.append(root.left)
                list.append(root.right)
            else:
                sympreorder.append(root)
        return sympreorder

    def isSymmetrical2(self, pRoot):
        # write code
        if pRoot is None:
            return True
        return self.isSubSym(pRoot.left,pRoot.right)

    def isSubSym(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            return root1.val == root2.val and self.isSubSym(root1.left,root2.right) and self.isSubSym(root1.right,root2.left)
        return False



if __name__ == "__main__":
    pRoot = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(6)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(7)
    node6 = TreeNode(5)
    pRoot.left = node1
    pRoot.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    sol = Solution()
    ans = sol.isSymmetrical2(pRoot)

    print(ans)