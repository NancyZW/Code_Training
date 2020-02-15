# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        list = []
        if len(matrix) == 0:
            return list
        rowNum = len(matrix)
        colNum = len(matrix[0])
        while len(list) < rowNum*colNum:
            list += matrix.pop(0)
            for i in range(len(matrix)):
                if matrix[i]:
                    list.append(matrix[i].pop())
            if matrix:
                list += matrix.pop()[::-1]
            for i in range(len(matrix)-1,0,-1):
                if matrix[i]:
                    list.append(matrix[i].pop(0))
        return list

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    sol = Solution()
    ans = sol.printMatrix(matrix)
    print(ans)