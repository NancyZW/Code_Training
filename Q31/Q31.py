# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        vec = []
        if len(pushV) == 0 and len(popV) == 0:
            return True
        while len(popV) != 0:
            popNode = popV[0]
            if len(vec) != 0 and vec[-1] == popNode:
                vec.pop()
                popV.pop(0)
                continue
            while len(pushV) != 0:
                node = pushV.pop(0)
                vec.append(node)
                if node == popNode:
                    break
            if len(pushV) == 0 and vec[-1] != popNode:
                return False
        return True

    def IsPopOrder2(self, pushV, popV):
        if len(popV) == 0 and len(pushV) == 0:
            return True
        vec = []
        while len(popV) != 0:
            if len(pushV) != 0 and popV[0] == pushV[-1]:
                popV.pop(0)
                pushV.pop()
            elif len(vec) != 0 and popV[0] == vec[-1]:
                vec.pop()
                popV.pop(0)
            elif len(pushV) != 0:
                vec.append(pushV.pop(0))
            else:
                return False
        return True




if __name__ == "__main__":
    pushV = [1,2,3,4,5]
    popV = [4,3,5,1,2]
    sol = Solution()
    ans = sol.IsPopOrder2(pushV,popV)
    print(ans)

