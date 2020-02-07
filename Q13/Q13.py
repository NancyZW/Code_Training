# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code
        n = 0
        visited = []
        res = self.RecursiveCount(threshold, rows, cols, 0, 0, visited)
        return res

    def RecursiveCount(self, threshold, rows, cols, x, y, visited):
        if x == -1 or x == rows or y == -1 or y == cols:
            return 0
        if not self.CheckThreshold(x,y,threshold):
            return 0
        if (x,y) in visited:
            return 0
        else:
            visited.append((x, y))
            return 1+self.RecursiveCount(threshold, rows, cols, x-1, y, visited)\
                +self.RecursiveCount(threshold, rows, cols, x+1, y, visited)\
                +self.RecursiveCount(threshold, rows, cols, x, y-1, visited)\
                +self.RecursiveCount(threshold, rows, cols, x, y+1, visited)

    def CheckThreshold(self,x,y,threshold):
        str_x = str(x)
        str_y = str(y)
        val = 0
        for i in str_x:
            val += int(i)
        for j in str_y:
            val += int(j)
        if val <= threshold:
            return True
        else:
            return False

# print(Solution().CheckThreshold(11,110111,6))
sol = Solution()
num = sol.movingCount(3,3,3)
print(num)