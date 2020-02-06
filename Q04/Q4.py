# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row_num = len(array)
        if row_num == 0:
            return False
        col_num = len(array[0])
        if col_num == 0:
            return False
        x = 0
        y = col_num-1
        val = array[x][y]
        while val != target:
            if val < target:
                if x == row_num-1:
                    return False
                x += 1
            else:
                if y == 0:
                    return False
                y -= 1
            val = array[x][y]
        return True
            
target = 7
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
sol = Solution()
ans = sol.Find(target, array)
print(ans)