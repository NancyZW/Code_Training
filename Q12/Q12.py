# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows == 0:
            return False
        matrix_array = []
        matrix_array = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        # print(matrix_array)

        idx = 0
        res = False
        for x in range(rows):
            for y in range(cols):
                p = []
                res = self.whetherexist(matrix_array, rows, cols, x, y, path, p)
                if res:
                    # print(p)
                    return True
        return False
    def whetherexist(self, matrix, rows, cols, x, y, path, p):
        # print(x,y)
        if (x,y) in p:
            return False
        if matrix[x][y] == path[0]:
            p.append((x,y))
            if len(path)==1:
                return True
        else:
            return False
        if x!=0 and self.whetherexist(matrix, rows, cols, x-1, y, path[1:], p):
            # p.append((x,y))
            return True
        if x!=rows-1 and self.whetherexist(matrix, rows, cols, x+1, y, path[1:], p):
            # p.append((x,y))
            return True
        if y!=0 and self.whetherexist(matrix, rows, cols, x, y-1, path[1:], p):
            # p.append((x,y))
            return True
        if y!=cols-1 and self.whetherexist(matrix, rows, cols, x, y+1, path[1:], p):
            # p.append((x,y))
            return True
        p.pop()
        return False


matrix = "AAAAAAAAAAAA"
# matrix = "abcesfcsadee"
# matrix = [['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
path = "AAAAAAAAAAAA"
# path = "abcb"
ans = Solution().hasPath(matrix,3,4,path)
print(ans)
